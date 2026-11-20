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


def bt_dang8_p4_b2_c10_hh9(self):
    k = random.choice([1, 2])
    R = 5 * k
    d1 = 3 * k
    r1 = 4 * k
    d2 = 4 * k
    r2 = 3 * k
    kc = d1 + d2

    noidungcauhoi = ('''Cho hình cầu tâm $O$ bán kính $R = %s\\text{ cm}$. Hai mặt phẳng song song $(P)$ và $(Q)$ nằm về hai phía đối với tâm $O$, lần lượt cắt hình cầu theo hai hình tròn có bán kính $r_1 = %s\\text{ cm}$ và $r_2 = %s\\text{ cm}$.\\\na) Tính khoảng cách từ tâm $O$ đến mỗi mặt phẳng $(P)$ và $(Q)$.\\\nb) Tính khoảng cách giữa hai mặt phẳng $(P)$ và $(Q)$.\\\nc) Tính tổng diện tích của hai hình tròn mặt cắt tạo bởi $(P)$ và $(Q)$.'''
                     % (R, r1, r2))

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Khoảng cách từ tâm $O$ đến mặt phẳng $(P)$ là:
$$d_1 = \\sqrt{R^2 - r_1^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}.$$
Khoảng cách từ tâm $O$ đến mặt phẳng $(Q)$ là:
$$d_2 = \\sqrt{R^2 - r_2^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}.$$
\\item Vì hai mặt phẳng song song $(P)$ và $(Q)$ nằm về hai phía khác nhau đối với tâm $O$ nên khoảng cách giữa chúng bằng:
$$h = d_1 + d_2 = %s + %s = %s\\text{ (cm)}.$$
\\item Diện tích hình tròn mặt cắt trên $(P)$ là: $S_1 = \\pi r_1^2 = %s\\pi\\text{ (cm}^2\\text{)}$.\\\nDiện tích hình tròn mặt cắt trên $(Q)$ là: $S_2 = \\pi r_2^2 = %s\\pi\\text{ (cm}^2\\text{)}$.\\\nTổng diện tích hai hình tròn mặt cắt là: $S = S_1 + S_2 = %s\\pi + %s\\pi = %s\\pi\\text{ (cm}^2\\text{)}$.
\\end{enumEX}'''
               % (R, r1, d1, R, r2, d2, d1, d2, kc, r1**2, r2**2, r1**2, r2**2, r1**2 + r2**2))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
