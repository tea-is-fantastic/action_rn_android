import os
import re

from scripts.tif_util import reg_rep, xmlpretty
from .utils import android_java, android_path, android_src


def bootsplash():
    reg_rep(os.path.join(android_path, 'build.gradle'),
            r'(minSdkVersion\s=\s)(\d{2})',
            r'\g<1>23')

    reg_rep(os.path.join(android_path, 'app', 'build.gradle'),
            r'^(\s+)(implementation.*swiperefresh.*\"\n)$',
            r'\1\2\1implementation "androidx.core:core-splashscreen:1.0.0"\n', flags=re.M,
            already='core-splashscreen')

    styl = """
  <!-- BootTheme should inherit from Theme.SplashScreen -->
  <style name="BootTheme" parent="Theme.SplashScreen">
    <item name="windowSplashScreenBackground">@color/bootsplash_background</item>
    <item name="windowSplashScreenAnimatedIcon">@mipmap/bootsplash_logo</item>
    <item name="postSplashScreenTheme">@style/AppTheme</item>
  </style>"""

    reg_rep(os.path.join(android_src, 'res', 'values', 'styles.xml'),
            r'(\s+)(<style name=\"AppTheme\".*</style>)',
            fr'\1\2\n{styl}', flags=re.DOTALL,
            already='bootsplash', callback=xmlpretty)

    reg_rep(os.path.join(android_src, 'AndroidManifest.xml'),
            r'@style/AppTheme',
            r'@style/BootTheme',
            already='BootTheme')

    reg_rep(os.path.join(android_java, 'MainActivity.java'),
            r'^(public class MainActivity)',
            r'import com.zoontek.rnbootsplash.RNBootSplash;\n\n\1',
            already='RNBootSplash')

    reg_rep(os.path.join(android_java, 'MainActivity.java'),
            r'^(s+)(super.onCreate)',
            r'\1RNBootSplash.init(this);\n\1\2',
            already='RNBootSplash')
