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



def bt_dang16_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [(12, 8, 20, Rational(24, 7)), (15, 10, 25, Rational(30, 7)), (18, 12, 30, Rational(36, 7))]
        R1, R2, R_hop, r_dien = random.choice(bo_so)
        D_hop = 2 * R_hop
        D1 = 2 * R1
        D2 = 2 * R2
        OO1 = R_hop - R1
        OO2 = R_hop - R2
        O1O2 = R1 + R2

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (O1) at (-1,0);
\\coordinate (O2) at (1.5,0);
\\coordinate (O3) at (0.357,1.62);
\\draw[line width=1pt] (O) circle (2.5cm);
\\draw[line width=1pt] (O1) circle (1.5cm);
\\draw[line width=1pt] (O2) circle (1cm);
\\draw[line width=1pt] (O3) circle (0.428cm);
\\draw[line width=1pt] (-2.5,0)--(2.5,0) (O1)--(O3)--(O2) (O)--(O3);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (O1) circle (1pt) node[below] {$O_1$};
\\fill (O2) circle (1pt) node[below] {$O_2$};
\\fill (O3) circle (1pt) node[above] {$O_3$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Một hộp kỹ thuật hình trụ tròn có đường kính trong là $%s\\text{ cm}$ dùng để đặt hai đường ống dẫn nước hình trụ song song chạy dọc theo chiều dài hộp. Ống cấp nước chính có đường kính ngoài $%s\\text{ cm}$ và ống thoát nước có đường kính ngoài $%s\\text{ cm}$.\\\\
        a) Chứng minh rằng có thể đặt vừa khít hai đường ống này vào bên trong hộp kỹ thuật sao cho cả hai ống đều tiếp xúc trong với thành hộp và tiếp xúc ngoài với nhau.\\\\
        b) Nếu người ta muốn luồn thêm một ống dây điện hình trụ vào khe hở sao cho ống này tiếp xúc ngoài với cả hai ống nước và tiếp xúc trong với thành hộp kỹ thuật, hãy tính bán kính tối đa $r$ của ống dây điện đó. %s'''
                         % (latex(D_hop), latex(D1), latex(D2), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item Xét mặt cắt ngang của hệ thống gồm đường tròn hộp kỹ thuật $(O; %s\\text{ cm})$, ống cấp nước $(O_1; %s\\text{ cm})$ và ống thoát nước $(O_2; %s\\text{ cm})$.\\\\
        Để $(O_1)$ và $(O_2)$ cùng tiếp xúc trong với $(O)$ tại hai đầu một đường kính của $(O)$ thì ba điểm $O_1, O, O_2$ thẳng hàng và $O$ nằm giữa $O_1, O_2$.\\\\
        Khi đó $OO_1 = R - R_1 = %s - %s = %s\\text{ cm}$ và $OO_2 = R - R_2 = %s - %s = %s\\text{ cm}$.\\\\
        Khoảng cách giữa hai tâm ống nước là $O_1O_2 = OO_1 + OO_2 = %s + %s = %s\\text{ cm}$.\\\\
        Mặt khác, tổng bán kính của hai ống nước là $R_1 + R_2 = %s + %s = %s\\text{ cm}$.\\\\
        Vì $O_1O_2 = R_1 + R_2$ nên hai ống nước tiếp xúc ngoài với nhau và nằm vừa khít bên trong hộp kỹ thuật.
        \\item Gọi $(O_3; r)$ là đường tròn mặt cắt của ống dây điện. Vì $(O_3)$ tiếp xúc ngoài với $(O_1), (O_2)$ và tiếp xúc trong với $(O)$ nên:\\\\
        $O_1O_3 = %s + r$; $O_2O_3 = %s + r$; $OO_3 = %s - r$.\\\\
        Áp dụng định lí Stewart cho tam giác $O_1O_2O_3$ với điểm $O$ nằm trên cạnh $O_1O_2$ (ta có $O_1O = %s$, $O_2O = %s$, $O_1O_2 = %s$):\\\\
        $O_1O_3^2 \\cdot O_2O + O_2O_3^2 \\cdot O_1O = O_1O_2 \\cdot (OO_3^2 + O_1O \\cdot O_2O)$\\\\
        $\\Leftrightarrow (%s + r)^2 \\cdot %s + (%s + r)^2 \\cdot %s = %s \\cdot [(%s - r)^2 + %s \\cdot %s]$.\\\\
        Khai triển và rút gọn phương trình bậc nhất theo $r$, ta tìm được bán kính tối đa của ống dây điện là $r = %s\\text{ (cm)}$.
        \\end{enumEX}'''
                   % (latex(R_hop), latex(R1), latex(R2),
                      latex(R_hop), latex(R1), latex(OO1), latex(R_hop), latex(R2), latex(OO2),
                      latex(OO1), latex(OO2), latex(O1O2), latex(R1), latex(R2), latex(O1O2),
                      latex(R1), latex(R2), latex(R_hop),
                      latex(OO1), latex(OO2), latex(O1O2),
                      latex(R1), latex(OO2), latex(R2), latex(OO1), latex(O1O2), latex(R_hop), latex(OO1), latex(OO2),
                      latex(r_dien)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
