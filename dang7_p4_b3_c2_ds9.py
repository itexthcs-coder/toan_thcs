import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang7_p4_b3_c2_ds9(self):
    while True:
        x_min = random.randint(-5, 0)
        x_max = x_min + random.randint(3, 6)

        a1 = random.randint(2, 5)
        c1 = random.randint(1, a1 - 1)
        b1 = random.randint(-8, 8)
        d1 = (a1 - c1) * x_min + b1

        m2 = random.randint(2, 4)
        a2 = random.randint(1, 3)
        c2 = random.randint(1, 4)
        b2 = m2 * c2 - a2 * x_max
        if b2 != 0:
            break

    tap_nghiem = [str(i) for i in range(x_min + 1, x_max + 1)]
    tap_nghiem_str = "; ".join(tap_nghiem)

    noidungcauhoi = (
        f"Tìm tất cả các số nguyên $x$ thỏa mãn đồng thời hai bất phương trình sau:\\\n"
        f"${latex(a1 * x + b1)} > {latex(c1 * x + d1)}$ và $\\dfrac{{{latex(a2 * x + b2)}}}{{{m2}}} \\le {c2}$."
    )

    loigiai = (
        f"Giải bất phương trình thứ nhất:\\\n"
        f"${latex(a1 * x + b1)} > {latex(c1 * x + d1)} \\Leftrightarrow {latex((a1 - c1) * x)} > {d1 - b1} \\Leftrightarrow x > {x_min}$.\\\n"
        f"Giải bất phương trình thứ hai:\\\n"
        f"$\\dfrac{{{latex(a2 * x + b2)}}}{{{m2}}} \\le {c2} \\Leftrightarrow {latex(a2 * x + b2)} \\le {m2 * c2} \\Leftrightarrow {latex(a2 * x)} \\le {m2 * c2 - b2} \\Leftrightarrow x \\le {x_max}$.\\\n"
        f"Kết hợp cả hai điều kiện, ta có ${x_min} < x \\le {x_max}$.\\\n"
        "Vì $x \\in \\mathbb{Z}$ nên $x \\in \\{" + tap_nghiem_str + "\\}$."
    )

    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
