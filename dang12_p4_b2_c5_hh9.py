# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:27:56 2024

@author: Pham Ngoc Chien
"""
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

def bt_dang12_p4_b2_c5_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R_str = '6,5'
        OH_str = '2,5'
        AB = 12
        rong_xe_str = '3,6'
        cao_xe_str = '5,8'

        noidungcauhoi = ('''Một đường hầm giao thông có mặt cắt ngang là một phần hình tròn tâm $O$, bán kính $R = %s\\text{ m}$ với mặt đường nằm ngang là dây cung $AB$ (như hình vẽ). Biết tâm $O$ nằm cao hơn mặt đường $AB$ một khoảng $OH = %s\\text{ m}$.\\\\
                         a) Tính chiều rộng $AB$ của mặt đường bên trong đường hầm.\\\\
                         b) Một xe tải chuyên dụng có chiều rộng $%s\\text{ m}$ và chiều cao $%s\\text{ m}$ chạy chính giữa đường hầm. Hỏi xe tải có đi qua hầm an toàn mà không chạm vào vòm hầm hay không? Vì sao?
                         \\begin{center}
                         \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                         \\coordinate (O) at (0,0);
                         \\coordinate (A) at (-1.66,-0.7);
                         \\coordinate (B) at (1.66,-0.7);
                         \\coordinate (H) at (0,-0.7);
                         \\draw[line width=1pt] (B) arc (-23:203:1.8);
                         \\draw[line width=1pt] (A)--(B);
                         \\draw[line width=1pt, dashed] (O)--(A) (O)--(B) (O)--(H);
                         \\fill (O) circle (1pt) node[above] {$O$};
                         \\fill (A) circle (1pt) node[left] {$A$};
                         \\fill (B) circle (1pt) node[right] {$B$};
                         \\fill (H) circle (1pt) node[below] {$H$};
                         \\end{tikzpicture}
                         \\end{center}'''
                         % (R_str, OH_str, rong_xe_str, cao_xe_str))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Vì tam giác $OAB$ cân tại $O$ có đường cao $OH$ nên $H$ là trung điểm của $AB$.\\\\
                        Áp dụng định lí Pythagore trong tam giác $OHA$ vuông tại $H$, ta có:\\\\
                        $AH = \\sqrt{OA^2 - OH^2} = \\sqrt{6,5^2 - 2,5^2} = \\sqrt{42,25 - 6,25} = \\sqrt{36} = 6\\text{ m}$.\\\\
                        Vậy chiều rộng của mặt đường bên trong đường hầm là $AB = 2AH = 2 \\cdot 6 = %s\\text{ m}$.
                        \\item Khi xe chạy chính giữa hầm, khoảng cách từ tim đường $H$ đến mép ngoài của xe là $\\dfrac{3,6}{2} = 1,8\\text{ m}$.\\\\
                        Gọi $M$ là điểm trên vòm hầm thẳng đứng phía trên mép ngoài của xe và $K$ là hình chiếu của $M$ trên đường thẳng qua $O$ song song với $AB$, ta có $OK = 1,8\\text{ m}$.\\\\
                        Áp dụng định lí Pythagore trong tam giác $OKM$ vuông tại $K$, ta có:\\\\
                        $MK = \\sqrt{OM^2 - OK^2} = \\sqrt{6,5^2 - 1,8^2} = \\sqrt{39,01} \\approx 6,25\\text{ m}$.\\\\
                        Chiều cao thông thủy của hầm tại vị trí mép ngoài của xe là $OH + MK \\approx 2,5 + 6,25 = 8,75\\text{ m} > 5,8\\text{ m}$.\\\\
                        Vậy xe tải đi qua đường hầm hoàn toàn an toàn.
                        \\end{enumEX}'''
                   % (AB))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
