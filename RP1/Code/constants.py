
#Zurich Bhanof Origin coordinates
LAT_REF = 47.3717306
LON_REF = 8.5386279
ALT_REF = 450

#Object detection model settings for yolo/tiny-yolo
options = {
                "model": "darkflow/cfg/yolo.cfg",
                "load": "darkflow/bin/yolov2.weights",
                "threshold": 0.6,
                "confidence":0.5,
                "labelsPath":"darkflow/coco.names"
            }
            
options_v3 = {
                "model": "darkflow/cfg/yolov3.cfg",
                "load": "darkflow/bin/yolov3.weights",
                "threshold": 0.8,
                "confidence":0.4,
                "labelsPath":"darkflow/coco.names"
            }

