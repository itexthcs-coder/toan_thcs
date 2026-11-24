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


def bt_dang1_p1_b1_c5_ds8(self):
    # Dạng 1: Nhận biết phương pháp thu thập dữ liệu trực tiếp
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        so_lan = random.choice([50, 80, 100, 120])
        ds_truc_tiep = [
            "Lập bảng hỏi và phát phiếu khảo sát cho học sinh trong trường",
            "Đứng tại cổng trường đếm số lượng học sinh đi xe đạp điện trong buổi sáng",
            "Thực hiện thí nghiệm gieo đồng xu $%s$ lần và ghi lại kết quả" % so_lan,
            "Phỏng vấn trực tiếp người dân về thói quen phân loại rác thải sinh hoạt",
            "Đo chiều cao và cân nặng của từng học sinh trong lớp $8A$"
        ]
        ds_gian_tiep = [
            "Tra cứu số liệu dân số trên trang web của Tổng cục Thống kê",
            "Đọc thông tin về diện tích các châu lục trong sách giáo khoa Địa lí",
            "Tổng hợp bảng xếp hạng bóng đá từ trang chủ của Liên đoàn Bóng đá Thế giới",
            "Lấy số liệu lượng mưa trung bình năm từ báo cáo trên cổng thông tin điện tử",
            "Tìm kiếm điểm chuẩn tuyển sinh lớp $10$ trên các trang báo điện tử",
            "Ghi chép nhiệt độ các thành phố lớn từ bản tin dự báo thời tiết trên truyền hình"
        ]
        
        da = random.choice(ds_truc_tiep)
        s = random.sample(ds_gian_tiep, 3)
        das1, das2, das3 = s[0], s[1], s[2]
        
        noidungcauhoi = ('''Phương pháp nào sau đây thuộc hình thức thu thập dữ liệu trực tiếp?''')
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('''Ta có định nghĩa về hai phương pháp thu thập dữ liệu:\\\\
- Thu thập dữ liệu trực tiếp là việc thu thập dữ liệu thông qua quan sát, làm thí nghiệm, lập bảng hỏi, phỏng vấn, đo đạc thực tế.\\\\
- Thu thập dữ liệu gián tiếp là việc thu thập dữ liệu từ những nguồn có sẵn như sách, báo, mạng Internet, báo cáo thống kê.\\\\
Do đó:\\\\
- Phương án "%s" là thu thập dữ liệu trực tiếp.\\\\
- Các phương án "%s", "%s" và "%s" đều lấy thông tin từ nguồn tài liệu hoặc trang thông tin có sẵn nên thuộc hình thức thu thập dữ liệu gián tiếp.'''
                   % (da, das1, das2, das3))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
