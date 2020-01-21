
#Zurich Bhanof Origin coordinates
LAT_REF = 47.3717306
LON_REF = 8.5386279
ALT_REF = 450

#Object detection model settings for yolo/tiny-yolo
options = {
                "model": "darkflow/cfg/yolo.cfg",
                "load": "darkflow/bin/yolo.weights",
                "threshold": 0.50,
            }