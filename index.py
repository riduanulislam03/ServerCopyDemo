# File: index.py
# Designed & Developed by Riduan Codex (@riduanulislam03)

import json
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_nid_info():
    # URL থেকে NID এবং জন্ম তারিখ (dob) সংগ্রহ করা
    nid_number = request.args.get('nid')
    dob = request.args.get('dob')
    
    # আপনার দেওয়া রেসপন্স ডাটা (ঠিক এই সিরিয়ালেই শো করবে)
    response_data = {
      "success": True,
      "status": "success",
      "message": "NID information retrieved successfully",
      "source": "nid",
      "data": {
        "id": 1128062,
        "nid": "6033003267",
        "pin": "20062699646000465",
        "formNo": "NIDFN121435517",
        "sl_no": "0",
        "father_nid": "8677284344",
        "mother_nid": "2619676129104",
        "religion": "Islam",
        "mobile": "MDE3MDEzNzk0MDg=",
        "voterNo": "262058698678",
        "voterArea": "মৈনারটেক (262058)",
        "education": "৪র্থ শ্রেণী",
        "occupation": "বেসরকারী চাকুরী",
        "status": "checked",
        "nameBangla": "মোহাম্মদ সোহান",
        "nameEnglish": "MOHAMMAD SOHAN",
        "dateOfBirth": "2006-01-12",
        "birthPlace": "ঢাকা",
        "fatherName": "মোঃ জজ মিয়া",
        "motherName": "মোসাঃ লাভলী বেগম",
        "spouseName": "",
        "gender": "male",
        "bloodGroup": "B+",
        "presentAddress": "বাসা/হোল্ডিংঃ ১১৮১৫০, গ্রাম/রাস্তাঃ মৈনারটেক, মৌজা/মহল্লাঃ উত্তরখান, ইউনিয়ন/ওয়ার্ডঃ ওয়ার্ড নং-৪৬, পোষ্ট অফিসঃ উজামপুর, পোষ্ট কোডঃ ১২৩০, উপজেলাঃ উত্তর খান, জেলাঃ ঢাকা, অঞ্চলঃ ঢাকা, বিভাগঃ ঢাকা",
        "permanentAddress": "বাসা/হোল্ডিংঃ ১১৮১৫০, গ্রাম/রাস্তাঃ মৈনারটেক, মৌজা/মহল্লাঃ উত্তরখান, ইউনিয়ন/ওয়ার্ডঃ ওয়ার্ড নং-৪৬, পোষ্ট অফিসঃ উজামপুর, পোষ্ট কোডঃ ১২৩০, উপজেলাঃ উত্তর খান, জেলাঃ ঢাকা, অঞ্চলঃ , বিভাগঃ ঢাকা",
        "address": "বাসা/হোল্ডিং: ১১৮/১৫০, গ্রাম/রাস্তা: মৈনারটেক, উত্তরখান, ডাকঘর: উজামপুর - ১২৩০, উত্তর খান, ঢাকা উত্তর সিটি কর্পোরেশন, ঢাকা",
        "created_at": "2026-08-26 10:06:49",
        "userIMG": "https://shurjoservice.online/sv_photos/img_9ae274afc906fa9344d085ba.jpg",
        "userSign": "https://api.svapi.net/admin_img/upload_6a8e9e982f15f5.92595532/img_6a8e9e998022c3.84451272.png"
      }
    }

    if nid_number:
        response_data["data"]["nid"] = nid_number
    if dob:
        response_data["data"]["dateOfBirth"] = dob

    # json.dumps দিয়ে ডিকশনারির অরিজিনাল সিরিয়াল ঠিক রাখা হচ্ছে এবং বাংলা ফন্ট ঠিক রাখতে ensure_ascii=False দেওয়া হয়েছে
    json_response = json.dumps(response_data, sort_keys=False, ensure_ascii=False)
    
    return Response(json_response, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
