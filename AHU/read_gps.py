from PIL import Image
import os
def get_exif_data(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    return exif_data


def get_location(exif_data):
    if not exif_data:
        return None
    # print(exif_data)
    gps_info = exif_data.get(0x8825)  # 34853 is the tag for 'GPSInfo'
    if gps_info:
        # 解析GPS信息（这里需要根据Exif规范来解析具体的纬度和经度值）
        # 注意：这个示例没有完全实现解析过程，需要根据实际的Exif格式来完成
        print("GPS信息:", gps_info)
    else:
        print("没有找到位置信息")


pic = os.listdir('pic')
for i in pic:
    image_path = 'pic/' + i
    exif_data = get_exif_data(image_path)
    get_location(exif_data)
# exif_data = get_exif_data(r"D:\Download\Edge\iCloud 照片\IMG_0853.JPEG")
# get_location(exif_data)
