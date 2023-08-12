from setuptools import setup

package_name = 'mr_firmware'
submodules = 'mr_firmware/submodules'
setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name,submodules],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Quantum Robotics',
    maintainer_email='eduardochavezmartin10@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'listener = mr_firmware.mr_driveteleop2_listener:main','listener_test = mr_firmware.mr_driveteleop2_listener_test:main',
        ],
    },
)
