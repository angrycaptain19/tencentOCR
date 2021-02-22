import json
import imageConvertToBase64 as ct
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models

def postToOCR(image_path):
    try:
        # Using own SecretID and SecretKey from tencent cloud
        cred = credential.Credential("AKIDbw2rSswX0HI3jKydNAi38xXv5yUkHGm2", "Ehx3tXv48vgJhxyibSvKThfOw2vVEiwv")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile

        # Using prefer region
        client = ocr_client.OcrClient(cred, "na-toronto", clientProfile)

        req = models.GeneralBasicOCRRequest()

        base64 = ct.convertToBase64(image_path)
        params = {"ImageBase64": base64
                  }


        req.from_json_string(json.dumps(params))
        resp = client.GeneralBasicOCR(req)

        #convert to json format
        resp = json.loads(resp.to_json_string())
        with open('static/respondJson/respond.json', 'w') as outfile:
            json.dump(resp, outfile)
        # with open('static/respondJson/respond.json', 'r') as fp:
        #     resp = json.load(fp)

        print(type(resp))
        return resp

    except TencentCloudSDKException as err:
        print(err)

# if __name__ == '__main__':
#     image_path = 'static/upload_images/file.jpg'
#     postToOCR(image_path)


