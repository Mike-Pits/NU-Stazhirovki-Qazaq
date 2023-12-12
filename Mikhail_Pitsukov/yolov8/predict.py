from PIL import Image
from ultralytics import YOLO

source_path = '/home/mikepi/Coding/NU/Stazhirovki/Qazaq_Stroy/data/test_One/'
# Load pretrained model
model = YOLO('/home/mikepi/Coding/NU/Stazhirovki/Qazaq_Stroy/scripts/Yolov8/runs/detect/train26/weights/best.pt')

# Run inference on test batch
results = model.predict('/home/mikepi/Coding/NU/Stazhirovki/Qazaq_Stroy/data/2_0/test_2/', show_labels=False, save=True, name='medium', save_crop=True)

# for r in results:
#     im_array = r.plot()  # plot a BGR numpy array of predictions
#     im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
#     im.show()  # show image