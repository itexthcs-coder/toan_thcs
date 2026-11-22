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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang20_p4_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        kc_km = 800
        thap_m = 25
        bong_m = 3.1
        bong_str = '3,1'

        deg_val = math.degrees(math.atan(bong_m / thap_m))
        do_a = int(deg_val)
        phut_a = int(Decimal(str((deg_val - do_a) * 60)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        cv_val = kc_km * (360.0 / deg_val)
        cv_str = str(int(Decimal(str(cv_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)))



        # Nội dung câu hỏi
        noidungcauhoi = ('''Vào khoảng năm 200 trước Công nguyên, nhà toán học và thiên văn học người Hy Lạp Eratosthenes đã ước lượng chu vi của Trái Đất nhờ hai quan sát vào đúng trưa ngày Hạ chí (21/6): \\\\
    - Tại thành phố Syene ($S$), tia sáng Mặt Trời chiếu thẳng đứng xuống tận đáy một chiếc giếng sâu. \\\\
    - Cùng lúc đó tại thành phố Alexandria ($A$) cách Syene $%s\\text{ km}$, một cột tháp thẳng đứng $AH$ cao $%s\\text{ m}$ đổ bóng trên mặt đất $AB$ dài $%s\\text{ m}$. \\\\
    Coi các tia nắng Mặt Trời chiếu tới Trái Đất là song song, mặt đất tại chân tháp vuông góc với thân tháp và Trái Đất có dạng hình cầu tâm $O$. \\\\
    a) Tính số đo góc ở tâm $\\widehat{SOA}$ chắn cung kinh tuyến từ Syene đến Alexandria (làm tròn đến phút). \\\\
    b) Từ kết quả trên, hãy trình bày cách tính và ước lượng chu vi của Trái Đất (làm tròn đến hàng đơn vị kilômét).''' % (kc_km, thap_m, bong_str))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Xét tam giác $HAB$ vuông tại $A$, ta có $\\tan \\widehat{AHB} = \\dfrac{AB}{AH} = \\dfrac{%s}{%s} = 0,124 \\Rightarrow \\widehat{AHB} \\approx %s^\\circ %s'$.\\\\
    Vì các tia nắng Mặt Trời chiếu tới Trái Đất song song với nhau nên $\\widehat{SOA} = \\widehat{AHB} \\approx %s^\\circ %s'$ (hai góc so le trong).
    \\item Trên đường tròn lớn của Trái Đất, độ dài cung tròn tỉ lệ thuận với góc ở tâm chắn cung đó.\\\\
    Một vòng tròn Trái Đất ứng với góc ở tâm $360^\\circ$, còn cung kinh tuyến $SA = %s\\text{ km}$ ứng với góc ở tâm $\\widehat{SOA}$.\\\\
    Do đó chu vi Trái Đất ước lượng được là $C = %s \\cdot \\dfrac{360^\\circ}{\\widehat{SOA}} \\approx %s\\text{ (km)}$.
    \\end{enumEX}'''
                   % (bong_str, thap_m, do_a, phut_a,
                      do_a, phut_a,
                      kc_km, kc_km, cv_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
