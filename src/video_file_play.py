import numpy as np
import cv2 as cv

import argparse

def main():
    parser = argparse.ArgumentParser(description='Play demo files with opencv',
                                     prog='video_file_play.py')
    parser.add_argument("-f", "--file", type=str, help='video file', default='../w251demo/afew_train_angry.avi')
    args = parser.parse_args()

    cap = cv.VideoCapture(args.file)
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        else:
            continue
        cv.imshow('frame',gray)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
