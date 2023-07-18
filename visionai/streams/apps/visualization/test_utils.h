#ifndef THIRD_PARTY_VISIONAI_STREAMS_APPS_VISUALIZATION_TEST_UTILS_H_
#define THIRD_PARTY_VISIONAI_STREAMS_APPS_VISUALIZATION_TEST_UTILS_H_

#include "opencv4/opencv2/core/mat.hpp"
namespace visionai {
namespace testutils {

// Checks if 2 OpenCV RGB images are exactly equal
bool CheckTwoImagesEqual(const cv::Mat& a, const cv::Mat& b);

}  // namespace testutils
}  // namespace visionai

#endif  // THIRD_PARTY_VISIONAI_STREAMS_APPS_VISUALIZATION_TEST_UTILS_H_

