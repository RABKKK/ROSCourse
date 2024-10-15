#include <opencv2/aruco.hpp>
#include "opencv2/highgui.hpp"
using namespace cv;
using namespace std;

int main()
{

Mat markerImage;
Ptr<cv::aruco::Dictionary> dictionary = aruco::getPredefinedDictionary(aruco::DICT_6X6_250);
aruco::drawMarker(dictionary, 23, 200, markerImage, 1);
imwrite("marker23.png", markerImage);

}

