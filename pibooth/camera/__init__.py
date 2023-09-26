# -*- coding: utf-8 -*-

from .. import utils
from .rpi import RpiCamera, get_rpi_camera_proxy
from .gphoto import GpCamera, get_gp_camera_proxy
from .opencv import CvCamera, get_cv_camera_proxy
from .hybrid import HybridRpiCamera, HybridCvCamera


def close_proxy(rpi_cam_proxy, gp_cam_proxy, cv_cam_proxy):
    """Close proxy drivers.
    """
    if rpi_cam_proxy:
        RpiCamera(rpi_cam_proxy).quit()
    if gp_cam_proxy:
        GpCamera(gp_cam_proxy).quit()
    if cv_cam_proxy:
        CvCamera(cv_cam_proxy).quit()


def find_camera():
    """Initialize the camera depending of the connected one. The priority order
    is chosen in order to have best rendering during preview and to take captures.
    The gPhoto2 camera is first (drivers most restrictive) to avoid connection
    concurence in case of DSLR compatible with OpenCV.
    """
    rpi_cam_proxy = get_rpi_camera_proxy()

    


    if rpi_cam_proxy:
        utils.LOGGER.info("Configuring Picamera camera ...")
        
        return RpiCamera(rpi_cam_proxy)

    raise EnvironmentError("Neither Raspberry Pi nor GPhoto2 nor OpenCV camera detected")
