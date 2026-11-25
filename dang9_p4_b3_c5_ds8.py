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

def bt_dang9_p4_b3_c5_ds8(self):
    # Dạng 9: Thiết kế và lựa chọn biểu đồ cho khảo sát đa tiêu chí trong trường học
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        mult = random.choice([1, 2])
        tong_hs = 320 * mult
        c1, c2, c3, c4 = 128 * mult, 96 * mult, 64 * mult, 32 * mult
        l1, l2, l3 = 210 * mult, 145 * mult, 185 * mult
        tong_luot = l1 + l2 + l3
        
        noidungcauhoi = ('Liên đội một trường THCS tiến hành khảo sát $%s$ học sinh khối $8$ và khối $9$ về thói quen đọc sách tại thư viện với hai câu hỏi:\n' % tong_hs +
                         '- \\textit{Câu hỏi 1:} "Em thường đọc thể loại sách nào nhất? (Chỉ chọn $1$ thể loại)". Kết quả: Truyện văn học ($%s$ bạn), Sách khoa học – khám phá ($%s$ bạn), Sách kĩ năng sống ($%s$ bạn), Báo – tạp chí học đường ($%s$ bạn).\n' % (c1, c2, c3, c4) +
                         '- \\textit{Câu hỏi 2:} "Em thường đến thư viện vào những khung giờ nào? (Có thể chọn nhiều phương án)". Kết quả: Giờ ra chơi buổi sáng ($%s$ lượt), Giờ nghỉ trưa ($%s$ lượt), Sau giờ tan học buổi chiều ($%s$ lượt).\n' % (l1, l2, l3) +
                         'a) Với dữ liệu thu được ở Câu hỏi $1$, hãy chọn loại biểu đồ thích hợp nhất để biểu diễn cơ cấu tỉ lệ học sinh chọn từng thể loại sách và tính các tỉ lệ phần trăm tương ứng.\\\n' +
                         'b) Có thể dùng biểu đồ hình quạt tròn để biểu diễn kết quả ở Câu hỏi $2$ không? Giải thích vì sao và đề xuất loại biểu đồ phù hợp thay thế.')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Ở Câu hỏi $1$, mỗi học sinh chỉ được chọn đúng một thể loại sách nên bốn nhóm kết quả tạo thành một tổng thể duy nhất ($%s + %s + %s + %s = %s$ học sinh). Loại biểu đồ thích hợp nhất để biểu diễn cơ cấu tỉ lệ này là \\textbf{biểu đồ hình quạt tròn}.\\\\' +
                   'Tỉ lệ phần trăm học sinh chọn từng thể loại sách là:\\\\' +
                   '- Truyện văn học: $\\dfrac{%s}{%s} \\cdot 100\\%% = 40\\%%$.\\\\' +
                   '- Sách khoa học – khám phá: $\\dfrac{%s}{%s} \\cdot 100\\%% = 30\\%%$.\\\\' +
                   '- Sách kĩ năng sống: $\\dfrac{%s}{%s} \\cdot 100\\%% = 20\\%%$.\\\\' +
                   '- Báo – tạp chí học đường: $\\dfrac{%s}{%s} \\cdot 100\\%% = 10\\%%$.\n' +
                   '\\item Không thể dùng biểu đồ hình quạt tròn để biểu diễn kết quả ở Câu hỏi $2$.\\\\' +
                   'Giải thích: Vì mỗi học sinh có thể chọn nhiều khung giờ nên tổng số lượt lựa chọn là $%s + %s + %s = %s > %s$ (vượt quá tổng số học sinh được hỏi, dẫn đến tổng các tỉ lệ phần trăm lớn hơn $100\\%%$). Trong trường hợp này, ta nên sử dụng \\textbf{biểu đồ cột} để biểu diễn.\n' +
                   '\\end{enumEX}'
                   ) % (c1, c2, c3, c4, tong_hs,
                        c1, tong_hs, c2, tong_hs, c3, tong_hs, c4, tong_hs,
                        l1, l2, l3, tong_luot, tong_hs)

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
