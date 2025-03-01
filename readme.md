## Bounding Box on objects using YOLOv5

The project uses YOLOv5 to detect objects in an image. The current threshold settings are 0.5.  

If you want to test it locally:
1. Clone the repo
2. Create a venv
3. Run `pip install -r requirements.txt`
4. Run the command: `streamlit run yolo.py`

### Results

1. Image in daylight conditions

![Daylight Image](https://github.com/prasannakotyal/yoloV5/blob/master/images/day.png)

2. Image in night conditions

![Night Image](https://github.com/prasannakotyal/yoloV5/blob/master/images/night.png)

3. Multiple images

![Multiple Images](https://github.com/prasannakotyal/yoloV5/blob/master/images/trio.png)

4. Image with noise around the main object

![Noisy Image](https://github.com/prasannakotyal/yoloV5/blob/master/images/fog.png)