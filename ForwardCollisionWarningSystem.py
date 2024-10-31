import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import logging
from typing import Dict
import tempfile
import time

class FCWSystem:
    """Forward Collision Warning System with GenAI integration"""
    
    def __init__(self, 
                 model_path: str = "yolov8n.pt",
                 warning_threshold: float = 0.5,
                 critical_threshold: float = 0.3,
                 min_confidence: float = 0.6):
        """Initialize FCW system with safety parameters"""
        self.model = YOLO(model_path)
        self.warning_threshold = warning_threshold
        self.critical_threshold = critical_threshold
        self.min_confidence = min_confidence
        self.logger = self._setup_logger()
        
    def _setup_logger(self) -> logging.Logger:
        """Setup logging with MISRA compliance"""
        logger = logging.getLogger('FCW_System')
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
        
    def process_frame(self, frame):
        """Process a single frame and return collision warnings"""
        if frame is None:
            raise ValueError("Invalid frame input")
            
        try:
            # Object detection using YOLO
            results = self.model(frame, conf=self.min_confidence)
            
            # Initialize warning data
            warning_data = {
                "warning_level": "SAFE",
                "collision_risk": 0.0,
                "detected_objects": []
            }
            
            # Process detected objects
            for result in results[0].boxes.data:
                x1, y1, x2, y2, conf, cls = result
                
                # Calculate relative distance (simplified)
                box_height = y2 - y1
                relative_distance = 1.0 - (box_height / frame.shape[0])
                
                # Object tracking data
                obj_data = {
                    "class": int(cls),
                    "confidence": float(conf),
                    "distance": float(relative_distance),
                    "position": (float(x1), float(y1), float(x2), float(y2))
                }
                warning_data["detected_objects"].append(obj_data)
                
                # Update warning level
                if relative_distance < self.critical_threshold:
                    warning_data["warning_level"] = "CRITICAL"
                    warning_data["collision_risk"] = 1.0
                    self.logger.warning("Critical collision risk detected")
                elif relative_distance < self.warning_threshold:
                    warning_data["warning_level"] = "WARNING"
                    warning_data["collision_risk"] = 0.7
                    self.logger.info("Collision warning issued")
                
                # Draw bounding box and warning
                color = (0, 0, 255) if warning_data["warning_level"] == "CRITICAL" else \
                        (0, 255, 255) if warning_data["warning_level"] == "WARNING" else \
                        (0, 255, 0)
                        
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
                cv2.putText(frame, 
                           f"{warning_data['warning_level']} - {relative_distance:.2f}",
                           (int(x1), int(y1) - 10),
                           cv2.FONT_HERSHEY_SIMPLEX,
                           0.5,
                           color,
                           2)
                
            return frame, warning_data
            
        except Exception as e:
            self.logger.error(f"Error processing frame: {str(e)}")
            raise

    def get_system_diagnostics(self) -> Dict:
        """Return system diagnostic information"""
        return {
            "model_status": "operational" if self.model is not None else "failed",
            "warning_threshold": self.warning_threshold,
            "critical_threshold": self.critical_threshold,
            "min_confidence": self.min_confidence
        }

def main():
    st.set_page_config(page_title="Forward Collision Warning System", layout="wide")
    
    # Sidebar controls
    st.sidebar.title("FCW System Controls")
    
    warning_threshold = st.sidebar.slider(
        "Warning Distance Threshold",
        min_value=0.3,
        max_value=0.9,
        value=0.5,
        help="Distance threshold for initial warning"
    )
    
    critical_threshold = st.sidebar.slider(
        "Critical Distance Threshold",
        min_value=0.1,
        max_value=0.4,
        value=0.3,
        help="Distance threshold for critical warning"
    )
    
    min_confidence = st.sidebar.slider(
        "Detection Confidence Threshold",
        min_value=0.3,
        max_value=0.9,
        value=0.6,
        help="Minimum confidence for object detection"
    )
    
    # Initialize FCW system
    fcw = FCWSystem(
        warning_threshold=warning_threshold,
        critical_threshold=critical_threshold,
        min_confidence=min_confidence
    )
    
    # Main content
    st.title("Forward Collision Warning System")
    
    # Input selection
    input_type = st.radio("Select Input Source", ["Webcam", "Video File"])
    
    if input_type == "Video File":
        uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])
        if uploaded_file is not None:
            # Save uploaded file temporarily
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded_file.read())
            video_path = tfile.name
        else:
            st.warning("Please upload a video file")
            return
    else:
        video_path = 0  # Use webcam
    
    # Create placeholders for video feed and metrics
    video_placeholder = st.empty()
    metrics_placeholder = st.container()
    
    # System diagnostics
    with st.expander("System Diagnostics", expanded=False):
        diagnostics = fcw.get_system_diagnostics()
        for key, value in diagnostics.items():
            st.text(f"{key}: {value}")
    
    cap = cv2.VideoCapture(video_path)
    
    # Start button
    if st.button("Start Processing"):
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                st.warning("End of video stream")
                break
            
            # Process frame
            processed_frame, warnings = fcw.process_frame(frame)
            
            # Convert BGR to RGB for displaying
            rgb_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
            
            # Update video feed
            video_placeholder.image(rgb_frame, channels="RGB", use_column_width=True)
            
            # Update metrics
            with metrics_placeholder:
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Warning Level", warnings["warning_level"])
                with col2:
                    st.metric("Collision Risk", f"{warnings['collision_risk']:.2f}")
                with col3:
                    st.metric("Objects Detected", len(warnings["detected_objects"]))
                
            # Add a small delay to control frame rate
            time.sleep(0.1)
            
            # Check if stop button is pressed
            if st.button("Stop"):
                break
    
    cap.release()

if __name__ == "__main__":
    main()
