from django.shortcuts import render
import re
import requests
from django.http import HttpResponse
import json
import datetime

from django.views.decorators.csrf import csrf_exempt

from validator.models import Vehicle


@csrf_exempt
def vehicle_validation(request):
    r = json.loads(request.body)
    image_path = r['path']

    url = "https://api.ocr.space/parse/image"

    payload = {'language': 'eng',
               'isOverlayRequired': 'false',
               'url': image_path,
               'iscreatesearchablepdf': 'false',
               'issearchablepdfhidetextlayer': 'false',
               'OCREngine': '2'}
    files = [
        ('url', open(image_path, 'rb'))
    ]
    headers = {
        'apikey': 'helloworld'
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    respnd = response.json()
    license_number = respnd['ParsedResults'][0]['ParsedText']
    license_number = license_number.replace('IL\n', '').replace(' ', '').replace(':', '').replace('-', '')
    license_number = license_number.splitlines()[0] # delete every thing after new line
    vehicle_type = get_type(license_number)
    is_valid = True
    if vehicle_type is not 'Other':
        is_valid = False

    vehicle = Vehicle(license_plate_number=license_number, type=vehicle_type, is_valid=is_valid, time_stamp=datetime.datetime.now())
    try:
        vehicle.save()
        response = json.dumps({'license number': vehicle.license_plate_number, 'type':vehicle.type, 'is_valid': vehicle.is_valid, 'time_stamp':str(datetime.datetime.now())})
    except:
        response = json.dumps({'Error': 'There was a problem with the request'})

    return HttpResponse(response, content_type='text/json')


def get_type(license_number):
    if license_number[-2:] in ('25', '26'):
        return 'Public transportation'
    elif re.search('[a-zA-Z]', license_number) is not None:
        return 'Military and law'
    elif len(license_number) == 7 and license_number[-2:] in ('85', '86', '87', '88', '89','00'):
        return '7 digit'

    sum = 0
    for c in license_number:
        if not c.isdigit():
            return 'Other'
        sum += int(c)

    if len(license_number) in (7, 8) and sum % 7 == 0:
        return 'Operated by gas'

    return 'Other'
