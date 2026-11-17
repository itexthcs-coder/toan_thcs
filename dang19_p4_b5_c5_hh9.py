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



def bt_dang19_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = randint(16, 22)
        R1 = randint(4, 6)
        R2 = randint(3, 5)
        OO1 = R - R1
        O1O2 = R1 + R2
        OO2 = abs(OO1 - O1O2)
        hieu_R_R2 = R - R2

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (O1) at (1.8,0);
\\coordinate (O2) at (0.6,0);
\\draw[line width=1pt] (O) circle (2.6cm);
\\draw[line width=1pt] (O1) circle (0.8cm);
\\draw[line width=1pt] (O2) circle (0.4cm);
\\draw[line width=1pt] (-2.6,0)--(2.6,0);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (O1) circle (1pt) node[below] {$O_1$};
\\fill (O2) circle (1pt) node[above] {$O_2$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Một nghệ nhân thiết kế mặt đồng hồ treo tường hình tròn tâm $O$, bán kính $R = %s\\text{ cm}$. Trên mặt đồng hồ có khoét một cửa sổ tròn lộ bộ máy cơ học (tâm $O_1$, bán kính $R_1 = %s\\text{ cm}$) và một mặt số phụ chỉ giây (tâm $O_2$, bán kính $R_2 = %s\\text{ cm}$). Biết rằng $O_1, O_2, O$ thẳng hàng theo thứ tự đó, cửa sổ lộ cơ tiếp xúc trong với viền đồng hồ $(O)$, còn mặt số phụ tiếp xúc ngoài với cửa sổ lộ cơ.\\\\
        a) Tính khoảng cách từ tâm đồng hồ $O$ đến tâm $O_1$ và tâm $O_2$.\\\\
        b) Xác định vị trí tương đối của mặt số phụ $(O_2)$ đối với viền ngoài của chiếc đồng hồ $(O)$. %s'''
                         % (latex(R), latex(R1), latex(R2), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item Vì cửa sổ lộ cơ $(O_1; %s\\text{ cm})$ tiếp xúc trong với viền đồng hồ $(O; %s\\text{ cm})$ nên khoảng cách giữa hai tâm là:\\\\
        $OO_1 = R - R_1 = %s - %s = %s\\text{ (cm)}$.\\\\
        Vì mặt số phụ $(O_2; %s\\text{ cm})$ tiếp xúc ngoài với cửa sổ lộ cơ $(O_1; %s\\text{ cm})$ nên khoảng cách giữa hai tâm này là:\\\\
        $O_1O_2 = R_1 + R_2 = %s + %s = %s\\text{ (cm)}$.\\\\
        Do $O_1, O_2, O$ thẳng hàng theo thứ tự đó nên điểm $O_2$ nằm giữa $O_1$ và $O$, suy ra:\\\\
        $OO_2 = |OO_1 - O_1O_2| = |%s - %s| = %s\\text{ (cm)}$.
        \\item Xét hai đường tròn $(O; %s\\text{ cm})$ và $(O_2; %s\\text{ cm})$, ta có hiệu hai bán kính là:\\\\
        $R - R_2 = %s - %s = %s\\text{ cm}$.\\\\
        Vì $OO_2 = %s\\text{ cm} < R - R_2 = %s\\text{ cm}$ nên đường tròn $(O)$ đựng đường tròn $(O_2)$ (hai đường tròn không giao nhau, mặt số phụ nằm hoàn toàn bên trong mặt đồng hồ).
        \\end{enumEX}'''
                   % (latex(R1), latex(R), latex(R), latex(R1), latex(OO1),
                      latex(R2), latex(R1), latex(R1), latex(R2), latex(O1O2),
                      latex(OO1), latex(O1O2), latex(OO2),
                      latex(R), latex(R2), latex(R), latex(R2), latex(hieu_R_R2),
                      latex(OO2), latex(hieu_R_R2)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
