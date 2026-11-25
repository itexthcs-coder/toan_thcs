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

def bt_dang1_p4_b3_c5_ds8(self):
    # Dạng 1: Phân tích biểu đồ đoạn thẳng so sánh số giờ chiếu nắng giữa hai bán cầu (Liên môn Địa lí)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        d_syd = random.choice([0, 5, 10])
        d_tok = random.choice([0, 5, 10])
        syd = [235 + d_syd, 205 + d_syd, 210 + d_syd, 195 + d_syd, 180 + d_syd, 165 + d_syd,
               190 + d_syd, 215 + d_syd, 220 + d_syd, 230 + d_syd, 225 + d_syd, 240 + d_syd]
        tok = [185 + d_tok, 170 + d_tok, 180 + d_tok, 185 + d_tok, 195 + d_tok, 150 + d_tok,
               165 + d_tok, 190 + d_tok, 155 + d_tok, 145 + d_tok, 150 + d_tok, 175 + d_tok]
        
        sum_syd = sum(syd)
        sum_tok = sum(tok)
        diff = sum_syd - sum_tok
        
        bang_latex = (
            '\\begin{center}\n' +
            '\\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|c|c|}\n' +
            '\\hline\n' +
            '\\textbf{Tháng} & $1$ & $2$ & $3$ & $4$ & $5$ & $6$ & $7$ & $8$ & $9$ & $10$ & $11$ & $12$ \\\\ \\hline\n' +
            '\\textbf{Sydney (giờ)} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \\hline\n' % tuple(syd) +
            '\\textbf{Tokyo (giờ)} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \\hline\n' % tuple(tok) +
            '\\end{tabular}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Số liệu từ biểu đồ đoạn thẳng ghi lại số giờ chiếu nắng trung bình tháng (đơn vị: giờ) trong năm tại hai thành phố Sydney (Úc) và Tokyo (Nhật Bản) được cho trong bảng thống kê sau:\n' +
                         bang_latex + '\n' +
                         'a) Tính tổng số giờ chiếu nắng trong cả năm của mỗi thành phố. Thành phố nào có tổng số giờ chiếu nắng trong năm nhiều hơn và nhiều hơn bao nhiêu giờ?\\\n' +
                         'b) Tìm ba tháng có số giờ chiếu nắng thấp nhất tại Sydney và ba tháng có số giờ chiếu nắng thấp nhất tại Tokyo. Vận dụng kiến thức Địa lí, hãy giải thích vì sao thời điểm ít nắng nhất trong năm của hai thành phố lại rơi vào các mùa khác nhau.')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Tổng số giờ chiếu nắng trong cả năm của Sydney là:\\\\' +
                   '$$%s + %s + %s + %s + %s + %s + %s + %s + %s + %s + %s + %s = %s \\text{ (giờ)}.$$\\\\' +
                   'Tổng số giờ chiếu nắng trong cả năm của Tokyo là:\\\\' +
                   '$$%s + %s + %s + %s + %s + %s + %s + %s + %s + %s + %s + %s = %s \\text{ (giờ)}.$$\\\\' +
                   'Vậy thành phố Sydney có tổng số giờ chiếu nắng nhiều hơn Tokyo và nhiều hơn: $%s - %s = %s$ (giờ).\n' +
                   '\\item Tại Sydney, ba tháng có số giờ chiếu nắng thấp nhất là Tháng $6$ ($%s$ giờ), Tháng $5$ ($%s$ giờ) và Tháng $7$ ($%s$ giờ).\\\\' +
                   'Tại Tokyo, ba tháng có số giờ chiếu nắng thấp nhất là Tháng $10$ ($%s$ giờ), Tháng $6$ ($%s$ giờ) và Tháng $11$ ($%s$ giờ).\\\\' +
                   'Giải thích: Sydney nằm ở Nam bán cầu nên khoảng thời gian từ tháng $5$ đến tháng $7$ là mùa đông (thời gian ban ngày ngắn, ít nắng). Ngược lại, Tokyo nằm ở Bắc bán cầu nên cuối thu – đầu đông (tháng $10$, tháng $11$) có số giờ nắng thấp, còn tháng $6$ tại Tokyo rơi vào mùa mưa đầu hè (mưa Baiu) nhiều mây mù làm giảm số giờ nắng.\n' +
                   '\\end{enumEX}'
                   ) % (tuple(syd) + (sum_syd,) + tuple(tok) + (sum_tok, sum_syd, sum_tok, diff, syd[5], syd[4], syd[6], tok[9], tok[5], tok[10]))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
