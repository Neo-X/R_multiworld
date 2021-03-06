import numpy as np

def create_sawyer_camera_init(
        lookat=(0, 0.85, 0.3),
        distance=0.3,
        elevation=-35,
        azimuth=270,
        trackbodyid=-1,
):
    def init(camera):
        camera.lookat[0] = lookat[0]
        camera.lookat[1] = lookat[1]
        camera.lookat[2] = lookat[2]
        camera.distance = distance
        camera.elevation = elevation
        camera.azimuth = azimuth
        camera.trackbodyid = trackbodyid

    return init


def init_sawyer_camera_v1(camera):
    """
    Do not get so close that the arm crossed the camera plane
    """
    camera.lookat[0] = 0
    camera.lookat[1] = 1
    camera.lookat[2] = 0.3
    camera.distance = 0.35
    camera.elevation = -35
    camera.azimuth = 270
    camera.trackbodyid = -1


def init_sawyer_camera_v2(camera):
    """
    Top down basically. Sees through the arm.
    """
    camera.lookat[0] = 0
    camera.lookat[1] = 0.8
    camera.lookat[2] = 0.3
    camera.distance = 0.3
    camera.elevation = -65
    camera.azimuth = 270
    camera.trackbodyid = -1


def init_sawyer_camera_v3(camera):
    """
    Top down basically. Sees through the arm.
    """
    camera.lookat[0] = 0
    camera.lookat[1] = 0.85
    camera.lookat[2] = 0.3
    camera.distance = 0.3
    camera.elevation = -35
    camera.azimuth = 270
    camera.trackbodyid = -1

def sawyer_xyz_camera(camera):
    camera.trackbodyid = 0
    camera.distance = 1.0

    # 3rd person view
    cam_dist = 0.3
    rotation_angle = 270
    cam_pos = np.array([0, 1.0, 0.5, cam_dist, -30, rotation_angle])

    for i in range(3):
        camera.lookat[i] = cam_pos[i]
    camera.distance = cam_pos[3]
    camera.elevation = cam_pos[4]
    camera.azimuth = cam_pos[5]
    camera.trackbodyid = -1

def sawyer_pusher_cam_v2(camera):

    camera.trackbodyid = 0
    camera.lookat[0] = 0
    camera.lookat[1] = 1.0
    camera.lookat[2] = 0.5
    camera.distance = 0.25
    camera.elevation = -50
    camera.azimuth = 270
    camera.trackbodyid = -1

def sawyer_pusher_cam_v3(camera):

    camera.trackbodyid = 0
    camera.lookat[0] = 0
    camera.lookat[1] = 0.9
    camera.lookat[2] = 0.4
    camera.distance = 0.25
    camera.elevation = -55
    camera.azimuth = 270
    camera.trackbodyid = -1

def sawyer_pusher_cam(camera):

    camera.trackbodyid = 0
    camera.lookat[0] = 0
    camera.lookat[1] = 0.95
    camera.lookat[2] = 0.45
    camera.distance = 1.5
    camera.elevation = -65
    camera.azimuth = 270
    camera.trackbodyid = -1



def sawyer_xyz_camera_v2(camera):
    camera.trackbodyid = 0
    camera.distance = 1.0

    # 3rd person view
    cam_dist = 0.3
    rotation_angle = 270
    cam_pos = np.array([0, 1.0, 0.65, cam_dist, -30, rotation_angle])

    for i in range(3):
        camera.lookat[i] = cam_pos[i]
    camera.distance = cam_pos[3]
    camera.elevation = cam_pos[4]
    camera.azimuth = cam_pos[5]
    camera.trackbodyid = -1

def sawyer_xyz_reacher_camera(camera):
    camera.trackbodyid = 0
    camera.distance = 1.0

    # 3rd person view
    cam_dist = .5
    rotation_angle = 270
    cam_pos = np.array([0, 1.0, 0.9, cam_dist, -45, rotation_angle])

    for i in range(3):
        camera.lookat[i] = cam_pos[i]
    camera.distance = cam_pos[3]
    camera.elevation = cam_pos[4]
    camera.azimuth = cam_pos[5]
    camera.trackbodyid = -1

def sawyer_door_env_camera_closer(camera):
    camera.trackbodyid = 0
    camera.distance = 1.0
    cam_dist = 0.1
    rotation_angle = 0
    cam_pos = np.array([0, 0.725, .9, cam_dist, -90, rotation_angle])

    for i in range(3):
        camera.lookat[i] = cam_pos[i]
    camera.distance = cam_pos[3]
    camera.elevation = cam_pos[4]
    camera.azimuth = cam_pos[5]
    camera.trackbodyid = -1