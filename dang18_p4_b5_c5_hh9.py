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



def bt_dang18_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = 10
        d_ngang = 22
        h_doc = 10
        O1O4_sq = (d_ngang // 2)**2 + h_doc**2
        O1O4_val = math.sqrt(O1O4_sq)
        O1O4_tron = str(Decimal(str(O1O4_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        
        alpha = math.acos(O1O4_val / (2 * R))
        S_quat = (R**2) * alpha
        S_tamgiac = 0.5 * O1O4_val * math.sqrt(R**2 - (O1O4_val / 2)**2)
        S_chung_val = 2 * (S_quat - S_tamgiac)
        S_chung_tron = str(Decimal(str(S_chung_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O1) at (0,0);
\\coordinate (O2) at (2.2,0);
\\coordinate (O3) at (4.4,0);
\\coordinate (O4) at (1.1,-1);
\\coordinate (O5) at (3.3,-1);
\\coordinate (H) at (1.1,0);
\\draw[line width=1pt] (O1) circle (1cm);
\\draw[line width=1pt] (O2) circle (1cm);
\\draw[line width=1pt] (O3) circle (1cm);
\\draw[line width=1pt] (O4) circle (1cm);
\\draw[line width=1pt] (O5) circle (1cm);
\\draw[line width=1pt, dashed] (O1)--(O2) (O1)--(O4) (O4)--(H);
\\fill (O1) circle (1pt) node[above] {$O_1$};
\\fill (O2) circle (1pt) node[above] {$O_2$};
\\fill (O3) circle (1pt) node[above] {$O_3$};
\\fill (O4) circle (1pt) node[below] {$O_4$};
\\fill (O5) circle (1pt) node[below] {$O_5$};
\\fill (H) circle (1pt) node[above] {$H$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Biểu tượng của Thế vận hội Olympic gồm $5$ vòng tròn bằng nhau có bán kính $R = %s\\text{ cm}$ đan xen vào nhau thành hai hàng: hàng trên gồm $3$ vòng tròn $(O_1), (O_2), (O_3)$ thẳng hàng và hàng dưới gồm $2$ vòng tròn $(O_4), (O_5)$ thẳng hàng. Biết khoảng cách giữa hai tâm liên tiếp trên cùng một hàng là $%s\\text{ cm}$, và khoảng cách từ đường thẳng nối tâm hàng trên xuống đường thẳng nối tâm hàng dưới là $%s\\text{ cm}$ (với $O_4$ nằm đối xứng giữa $O_1, O_2$ và $O_5$ nằm đối xứng giữa $O_2, O_3$).\\\\
        a) Xét vị trí tương đối của $(O_1)$ với $(O_2)$, và của $(O_1)$ với $(O_4)$.\\\\
        b) Tính diện tích phần đan xen (phần chung) giữa hai hình tròn $(O_1)$ và $(O_4)$ (làm tròn đến hàng phần mười theo đơn vị $\\text{cm}^2$). %s'''
                         % (latex(R), latex(d_ngang), latex(h_doc), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item - Xét $(O_1; %s\\text{ cm})$ và $(O_2; %s\\text{ cm})$: Ta có $O_1O_2 = %s\\text{ cm} > R + R = %s\\text{ cm}$.\\\\
        Vậy hai đường tròn $(O_1)$ và $(O_2)$ ở ngoài nhau (không giao nhau).\\\\
        - Gọi $H$ là hình chiếu vuông góc của $O_4$ lên $O_1O_2$. Vì $O_4$ nằm đối xứng giữa $O_1, O_2$ nên $H$ là trung điểm của $O_1O_2$, suy ra $O_1H = \\frac{%s}{2} = 11\\text{ cm}$ và $O_4H = %s\\text{ cm}$.\\\\
        Áp dụng định lí Pythagore vào tam giác vuông $O_1HO_4$, ta có:\\\\
        $O_1O_4 = \\sqrt{O_1H^2 + O_4H^2} = \\sqrt{11^2 + %s^2} = \\sqrt{%s} \\approx %s\\text{ (cm)}$.\\\\
        Vì $R - R = 0 < O_1O_4 < R + R = %s\\text{ cm}$ nên hai đường tròn $(O_1)$ và $(O_4)$ cắt nhau tại hai điểm phân biệt.
        \\item Gọi $A, B$ là hai giao điểm của $(O_1)$ và $(O_4)$. Trong tam giác cân $O_1AB$ có đường cao $O_1M = \\frac{O_1O_4}{2} = \\frac{\\sqrt{%s}}{2}$, ta có $\\cos \\widehat{AO_1M} = \\frac{\\sqrt{%s}}{2 \\cdot %s}$.\\\\
        Diện tích một nửa phần chung (viên phân tròn) là hiệu diện tích hình quạt $O_1AB$ và diện tích tam giác $O_1AB$:\\\\
        $S_{\\text{viên phân}} = \\frac{\\pi \\cdot %s^2 \\cdot 2\\widehat{AO_1M}}{360^\\circ} - \\frac{1}{2} \\cdot %s^2 \\cdot \\sin(2\\widehat{AO_1M})$.\\\\
        Do hai hình tròn bằng nhau nên diện tích phần chung của $(O_1)$ và $(O_4)$ là: $S = 2 S_{\\text{viên phân}} \\approx %s\\text{ (cm}^2\\text{)}$.
        \\end{enumEX}'''
                   % (latex(R), latex(R), latex(d_ngang), latex(2*R),
                      latex(d_ngang), latex(h_doc), latex(h_doc), latex(O1O4_sq), O1O4_tron, latex(2*R),
                      latex(O1O4_sq), latex(O1O4_sq), latex(R),
                      latex(R), latex(R), S_chung_tron))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
