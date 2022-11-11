import os
import re

from scripts.tif_util import reg_rep
from .utils import android_java


def navigation():
    code = """@Override
    protected void onCreate(Bundle savedInstanceState) {
      super.onCreate(null);
    }"""

    reg_rep(os.path.join(android_java, 'MainActivity.java'),
            r'^(public class MainActivity)',
            r'import android.os.Bundle;\n\n\1',
            already='android.os.Bundle')

    reg_rep(os.path.join(android_java, 'MainActivity.java'),
            r'^(public class MainActivity)',
            fr'\1\n\n{code}',
            already='void onCreate')
