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


def bt_dang17_p3_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r = randint(5, 45)
        tong_day = 4 * r
        kq_str = str(tong_day)

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O1) at (-1.2,0);
\\coordinate (O2) at (1.2,0);
\\coordinate (A) at (-1.2,1.2);
\\coordinate (B) at (1.2,1.2);
\\coordinate (C) at (-1.2,-1.2);
\\coordinate (D) at (1.2,-1.2);
\\draw[line width=1pt] (O1) circle (1.2);
\\draw[line width=1pt] (O2) circle (1.2);
\\draw[line width=1pt] (A)--(B) (C)--(D);
\\draw[line width=1pt, dashed] (O1)--(O2) (O1)--(A) (O2)--(B) (O1)--(C) (O2)--(D);
\\draw[line width=1pt] (-1.2,0.95)--(-0.95,0.95)--(-0.95,1.2);
\\draw[line width=1pt] (1.2,0.95)--(0.95,0.95)--(0.95,1.2);
\\fill (O1) circle (1pt) node[below left] {$O_1$};
\\fill (O2) circle (1pt) node[below right] {$O_2$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Người ta dùng một sợi dây đai bó sát quanh hai ống nước hình trụ giống hệt nhau đặt nằm ngang tiếp xúc ngoài với nhau trên mặt đất, mỗi ống có bán kính $R = %s\\text{ cm}$ (bỏ qua độ dày dây đai). Biết hai đoạn dây thẳng phía trên và phía dưới là các tiếp tuyến chung của hai đường tròn mặt cắt. Tính tổng chiều dài hai đoạn dây thẳng đó (đơn vị: cm).'''
                         %(str(r)))
        
        # Nội dung lời giải
        loigiai = ('''%s 
Gọi $(O_1; %s\\text{ cm})$ và $(O_2; %s\\text{ cm})$ là hai đường tròn mặt cắt của hai ống nước. Vì hai ống tiếp xúc ngoài với nhau nên khoảng cách hai tâm là: $O_1O_2 = 2R = 2 \\cdot %s = %s\\text{ (cm)}$. \\\\
Gọi $AB$ và $CD$ là hai đoạn dây thẳng tiếp xúc chung với cả hai đường tròn tại $A, B, C, D$. \\\\
Vì $AB$ là tiếp tuyến chung của $(O_1)$ và $(O_2)$ nên $O_1A \\perp AB$ và $O_2B \\perp AB$. Lại có $O_1A = O_2B = R$ nên tứ giác $O_1ABO_2$ là hình chữ nhật, suy ra $AB = O_1O_2 = %s\\text{ cm}$. \\\\
Tương tự, $CD = O_1O_2 = %s\\text{ cm}$. \\\\
Vậy tổng chiều dài hai đoạn dây thẳng là: $AB + CD = %s + %s = %s\\text{ (cm)}$.'''
                   %(hinhve, str(r), str(r), str(r), str(2*r), str(2*r), str(2*r), str(2*r), str(2*r), str(tong_day)))
        
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(str(kq_str))

    # Xuất câu hỏi trả lời ngắn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
