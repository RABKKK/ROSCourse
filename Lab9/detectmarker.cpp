
#include "opencv2/imgproc.hpp"

#include "opencv2/videoio.hpp"

#include <opencv2/aruco.hpp>
#include "opencv2/highgui.hpp"

#include <iostream>
#include <opencv2/calib3d.hpp>

using namespace cv;
using namespace std;

void drawText(Mat & image, vector<int> markerIds);

int main()
{

	Mat inputImage;
	vector<int> markerIds;
	vector<vector<Point2f>> markerCorners, rejectedCandidates;
	Ptr<aruco::DetectorParameters> parameters = aruco::DetectorParameters::create();
	Ptr<cv::aruco::Dictionary> dictionary = aruco::getPredefinedDictionary(aruco::DICT_6X6_250);

	Mat cameraMatrix, distCoeffs;
	cameraMatrix=Mat::eye(3,3,CV_32F);
	distCoeffs=Mat::zeros(1,5,CV_32F);
        
        //Camera parameters will be based on the camera that is used
        //cameraMatrix.at<float>(0,2) will be approx half of image horizontal size
        //cameraMatrix.at<float>(1,2) will be approx half of image vertical size
	cameraMatrix.at<float>(0,0)=500.00;//approx value for general cases
	//cameraMatrix.at<float>(0,2)=320.00;
	cameraMatrix.at<float>(1,1)=500.00;//approx value for general cases
	//cameraMatrix.at<float>(1,2)=240.00;



	Mat image;
	VideoCapture capture;
	capture.open(0);
	if(capture.isOpened())
	{
	  cout << "Capture is opened" << endl;
	  for(;;){
	    capture >> image;
	    //cout<<image.size();//CHeck image size
	    if(image.empty())
	    break;
	    aruco::detectMarkers(image, dictionary, markerCorners, markerIds, parameters, rejectedCandidates);
	    Mat outputImage = image.clone();
	    if (markerIds.size()>0) {
	      vector<cv::Vec3d> rvecs, tvecs;
	      aruco::drawDetectedMarkers(outputImage, markerCorners, markerIds);                        
	      aruco::estimatePoseSingleMarkers(markerCorners, 0.05, cameraMatrix, distCoeffs, rvecs, tvecs);
	      cout<<"Orientation"<<rvecs[0]<<"Translation"<<tvecs[0]<<endl;
	      for (int i = 0; i < rvecs.size(); ++i) {
	      auto rvec = rvecs[i];
	      auto tvec = tvecs[i];
	      drawFrameAxes(outputImage, cameraMatrix, distCoeffs, rvec, tvec, 0.1);
	      }
	    }
	    else{
	    drawText(outputImage, markerIds);
	    }
	    imshow("Output Image", outputImage);
		    if(waitKey(10) >= 0)
		        break;
		}
	    }
	else{
	  cout << "No capture" << endl;
	  image = Mat::zeros(480, 640, CV_8UC1);
	  drawText(image, markerIds);
	  imshow("Sample", image);
	  waitKey(0);
	}
    return 0;
}

void drawText(Mat & image, vector<int> markerIds)
{
    if (markerIds.size()>0)
    {
    string strid=to_string(markerIds.at(0));
    putText(image, strid, Point(20, 50), FONT_HERSHEY_COMPLEX, 1, // font face and scale
            Scalar(255, 255, 255), // white
            1, LINE_AA); // line thickness and type
    }
      else {
           putText(image, "Not Detected", Point(20, 50), FONT_HERSHEY_COMPLEX, 1, // font face and scale
            Scalar(255, 255, 255), // white
            1, LINE_AA); // line thickness and type

      }             
}
