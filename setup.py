from setuptools import setup, find_packages, Extension
import glob
import os.path
import sys


C_SRC_PREFIX = os.path.join('cbits', 'webrtc', 'common_audio')
C_SRC_RTC_PREFIX = os.path.join('cbits', 'webrtc', 'rtc_base')

c_sources = (
    [os.path.join(
        'cbits', 'pywebrtcvad.c')]
    + glob.glob(
        os.path.join(
            C_SRC_PREFIX,
            'signal_processing',
            '*.c'))
    + glob.glob(
        os.path.join(
            C_SRC_PREFIX,
            'third_party',
            '*.c'))
    + glob.glob(
        os.path.join(
            C_SRC_PREFIX,
            'vad',
            '*.c'))
)

define_macros = []
extra_compile_args = []

if sys.platform.startswith('win'):
    define_macros.extend([('_WIN32', None), ('WEBRTC_WIN', None)])
else:
    define_macros.extend([('WEBRTC_POSIX', None), ])
    extra_compile_args.extend(['-std=c11'])

module = Extension('_vad_nc',
                   define_macros=define_macros,
                   extra_compile_args=extra_compile_args,
                   sources=c_sources,
                   include_dirs=['cbits'])

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='vad-nc',
    author='Rivaille Lee',
    author_email='xxxxx@gmail.com',
    version='1.0.0.dev0',
    description=('Python interface to the Google WebRTC Voice '
                 'Activity Detector (VAD) added with some wave Data Preprocessing modules'),
    long_description=long_description,
    url='xxx',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular,
        # ensure that you indicate whether you support Python 2,
        # Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='speechrecognition asr voiceactivitydetection vad webrtc noise-reduction',
    ext_modules=[module],
    py_modules=['webrtcvad'],
    test_suite='nose.collector',
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example: $ pip install -e .[test,doc]
    extras_require={
        'test': ['nose', 'check-manifest', 'unittest2', 'zest.releaser',
                'psutil', 'memory_profiler']
    }
)
