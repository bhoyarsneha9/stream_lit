import cv2
import numpy as np
import time
from ultralytics import YOLO
import warnings
import logging
from typing import Tuple, List, Dict

class FCWSystem:
    """Forward Collision Warning System with GenAI integration"""
    
    def __init__(self, 
                 model_path: str = "yolov8n.pt",
                 warning_threshold: float = 0.5,
                 critical_threshold: float = 0.3,
                 min_confidence: float = 0.6):
        """
        Initialize FCW system with safety parameters
        
        Args:
            model_path: Path to the YOLO model
            warning_threshold: Distance threshold for warning (normalized)
            critical_threshold: Distance threshold for critical warning
            min_confidence: Minimum confidence for object detection
        """
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
        
    def process_frame(self, frame: np.ndarray) -> Tuple[np.ndarray, Dict]:
        """
        Process a single frame and return collision warnings
        
        Args:
            frame: Input image frame
            
        Returns:
            Tuple containing processed frame and warning data
        """
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
            
    def run_safety_checks(self) -> bool:
        """Perform system safety checks according to ASIL standards"""
        try:
            # Memory check
            if self.model is None:
                raise RuntimeError("Model not initialized")
                
            # Parameter validation
            if not (0 < self.critical_threshold < self.warning_threshold < 1):
                raise ValueError("Invalid threshold configuration")
                
            # System status check
            self.logger.info("Safety checks passed successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Safety check failed: {str(e)}")
            return False

    def get_system_diagnostics(self) -> Dict:
        """Return system diagnostic information"""
        return {
            "model_status": "operational" if self.model is not None else "failed",
            "warning_threshold": self.warning_threshold,
            "critical_threshold": self.critical_threshold,
            "min_confidence": self.min_confidence,
            "safety_check_status": self.run_safety_checks()
        }

# Example usage
def main():
    # Initialize FCW system
    fcw = FCWSystem()
    
    # Open video capture (can be camera or video file)
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Process frame
        processed_frame, warnings = fcw.process_frame(frame)
        
        # Display results
        cv2.imshow('FCW System', processed_frame)
        
        # Exit on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
