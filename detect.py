import torch
from PIL import Image

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path='./models/batch8_epoch40_v5l_f1.pt')


img1 = Image.open('./data/test1.jpg')
img2 = Image.open('./data/test2.jpg')
imgs = [img1, img2]  # batch of images

# Inference
model.eval()
results = model(imgs)  # includes NMS

# Results
print(results)
results.print()
results.save('./sdfsdf')
crops = results.crop('./sdfsdf')  # cropped detections dictionary
# results.show()
print('\n===img1 predictions (tensor)===')
print(results.xyxy[0])  # img1 predictions (tensor)
print('========\n')
print('===img1 predictions (pandas)===')
print(results.pandas().xyxy[0].xmin[0])  # img1 predictions (pandas)
print('========\n')
