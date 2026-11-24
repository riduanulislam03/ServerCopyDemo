# File: index.py
# Developed by Riduan Codex (@riduanulislam03)

import json
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/api/server/server-copy', methods=['GET'])
def get_nid_info():
    # URL থেকে nid, dob এবং secretKey সংগ্রহ করা
    nid_number = request.args.get('nid')
    dob = request.args.get('dob')
    secret_key = request.args.get('secretKey')
    
    # আপনার দেওয়া ১০০% হুবহু রেসপন্স ডাটা (একই সিরিয়ালে শো করবে)
    response_data = {
      "success": True,
      "status": "success",
      "message": "NID information retrieved successfully",
      "source": "api",
      "data": {
        "name": "রিদুয়ানুল ইসলাম",
        "nameEn": "RIDUANUL ISLAM",
        "gender": "male",
        "father": "মোঃ নুরুল ইসলাম",
        "mother": "রোকেয়া বেগম ছিদ্দিকা",
        "nationalId": "8282169989",
        "pin": "20031528202000161",
        "oldNid": "1528202000161",
        "voter_no": "152526531445",
        "voter_area_code": "152526",
        "sl_no": "3538",
        "voterArea": "সোনাকানিয়া (152526)",
        "occupation": "শ্রমিক",
        "bloodGroup": "",
        "birthPlace": "চট্টগ্রাম",
        "dateOfBirth": "2003-05-09",
        "birthDay": "শুক্রবার",
        "age": "২৩ বছর ৬ মাস ১৫ দিন",
        "presentAddress": "বাসা/হোল্ডিংঃ ৮১৯, গ্রাম/রাস্তাঃ মাইজ পাড়া, সোনাকানিয়া (০২ নং ওয়ার্ড সোনাকানিয়া এলাকা অংশ), ওয়ার্ড নংঃ ০২, মৌজা/মহল্লাঃ সোনাকানিয়া, সিটি কর্পোরেশন/পৌরসভাঃ সাতকানীয়া পৌরসভা, পোস্ট কোডঃ ৪৩৮৬, থানাঃ সাতকানিয়া, উপজেলাঃ সাতকানিয়া, জেলাঃ চট্টগ্রাম, বিভাগঃ চট্টগ্রাম।",
        "permanentAddress": "বাসা/হোল্ডিংঃ ৮১৯, গ্রাম/রাস্তাঃ মাইজ পাড়া, সোনাকানিয়া (০২ নং ওয়ার্ড সোনাকানিয়া এলাকা অংশ), ওয়ার্ড নংঃ ০২, মৌজা/মহল্লাঃ সোনাকানিয়া, সিটি কর্পোরেশন/পৌরসভাঃ সাতকানীয়া পৌরসভা, পোস্ট কোডঃ ৪৩৮৬, থানাঃ সাতকানিয়া, উপজেলাঃ সাতকানিয়া, জেলাঃ চট্টগ্রাম, বিভাগঃ চট্টগ্রাম।",
        "permanentAddr": {
          "division": "চট্টগ্রাম",
          "district": "চট্টগ্রাম",
          "upozila": "সাতকানিয়া",
          "postOffice": "",
          "postalCode": "",
          "mouzaOrMoholla": "সোনাকানিয়া",
          "villageOrRoad": "মাইজ পাড়া, সোনাকানিয়া",
          "homeOrHolding": "৮১৯",
          "region": ""
        },
        "presentAddr": {
          "division": "চট্টগ্রাম",
          "district": "চট্টগ্রাম",
          "upozila": "সাতকানিয়া",
          "postOffice": "",
          "postalCode": "",
          "mouzaOrMoholla": "সোনাকানিয়া",
          "villageOrRoad": "মাইজ পাড়া, সোনাকানিয়া",
          "homeOrHolding": "৮১৯",
          "region": ""
        },
        "photo": "https://api.svapi.icu/images/824e3920c3931b3c38f1a53f6c54a8fc.jpg"
      },
      "billing": {
        "name": "surjo",
        "today_hit": 141,
        "today_success": 73,
        "today_cost": 949,
        "total_success": 138,
        "total_bill": 1794,
        "speed": "1.389s",
        "charged": 17,
        "balance": 133
      }
    }

    if nid_number:
        response_data["data"]["nationalId"] = nid_number
    if dob:
        response_data["data"]["dateOfBirth"] = dob

    # json.dumps দিয়ে ডিকশনারির অরিজিনাল সিরিয়াল এবং বাংলা ফন্ট ঠিক রাখা হয়েছে
    json_response = json.dumps(response_data, sort_keys=False, ensure_ascii=False)
    
    return Response(json_response, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
