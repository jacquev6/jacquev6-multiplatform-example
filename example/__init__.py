import platform

from libexample import add


for name in [
    # Cross platform:
    "architecture",
    "machine",
    "platform",
    "processor",
    "python_build",
    "python_compiler",
    "python_branch",
    "python_implementation",
    "python_revision",
    "python_version",
    "release",
    "system",
    "version",
    # Platform specific:
    "win32_ver", "win32_edition", "win32_is_iot",
    "mac_ver",
    "ios_ver",
    "libc_ver",
    "freedesktop_os_release",
    "android_ver",
]:
    try:
        print(f"{name:33}:", getattr(platform, name)())
    except Exception as e:
        print(f"{name:24} (failed): {e}")


assert add(4, 5) == 9

print("'jacquev6-multiplatform-example' imported successfully")
