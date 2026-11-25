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

def bt_dang2_p1_b3_c5_ds8(self):
    # Dạng 2: Nhận diện phương pháp thu thập dữ liệu
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        gio1 = random.choice(['$6\\text{h}30$', '$6\\text{h}45$', '$11\\text{h}15$', '$16\\text{h}45$'])
        gio2 = random.choice(['$7\\text{h}00$', '$7\\text{h}15$', '$11\\text{h}45$', '$17\\text{h}15$'])
        
        scenarios = [
            ('Bác bảo vệ ngồi tại cổng trường từ %s đến %s và đánh dấu vào sổ xem có bao nhiêu học sinh đi học bằng xe đạp điện, xe đạp thường hoặc đi bộ.' % (gio1, gio2),
             'quan sát trực tiếp',
             'Bác bảo vệ trực tiếp theo dõi hành vi thực tế của học sinh tại cổng trường và ghi chép lại mà không đặt câu hỏi hay phát phiếu.'),
            ('Bạn Nam đứng ở hành lang tầng hai từ %s đến %s và ghi chép lại xem có bao nhiêu bạn đi sang đường sử dụng cầu vượt khi tan trường.' % (gio1, gio2),
             'quan sát trực tiếp',
             'Bạn Nam đứng từ xa theo dõi và ghi nhận trực tiếp hành động thực tế của các bạn học sinh.'),
            ('Một nhóm học sinh lớp $8$ đến từng bàn trong căng tin, hỏi trực tiếp các bạn đang ăn trưa về món ăn yêu thích nhất rồi ghi lại câu trả lời.',
             'phỏng vấn trực tiếp',
             'Nhóm học sinh đặt câu hỏi trực tiếp cho từng đối tượng khảo sát và ghi nhận câu trả lời.'),
            ('Lớp trưởng phát cho mỗi bạn trong lớp một tờ giấy in sẵn các câu hỏi về sở thích đọc sách để các bạn tự điền thông tin rồi thu lại.',
             'lập phiếu hỏi',
             'Lớp trưởng sử dụng phiếu khảo sát in sẵn câu hỏi để người được hỏi tự điền phương án trả lời.'),
            ('Bạn Lan truy cập trang web chính thức của Tổng cục Thống kê để lấy bảng số liệu về dân số Việt Nam qua các năm.',
             'khai thác từ nguồn có sẵn',
             'Bạn Lan thu thập dữ liệu đã được cơ quan chức năng thống kê, tổng hợp và công bố sẵn trên trang thông tin chính thống.')
        ]
        
        sc = random.choice(scenarios)
        mota, da, giaithich = sc
        
        all_methods = [
            'quan sát trực tiếp',
            'phỏng vấn trực tiếp',
            'lập phiếu hỏi',
            'khai thác từ nguồn có sẵn',
            'làm thí nghiệm khoa học'
        ]
        s_pool = [m for m in all_methods if m != da]
        das1 = random.choice(s_pool)
        s_pool.remove(das1)
        das2 = random.choice(s_pool)
        s_pool.remove(das2)
        das3 = random.choice(s_pool)
        
        noidungcauhoi = ('%s Phương pháp thu thập dữ liệu được sử dụng trong tình huống trên là' % mota)
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('%s\\\\' +
                   'Vậy phương pháp thu thập dữ liệu được sử dụng là %s.'
                   ) % (giaithich, da)

    # Xuất câu trắc nghiệm
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
