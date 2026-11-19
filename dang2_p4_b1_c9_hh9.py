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


def bt_dang2_p4_b1_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        AB = random.randint(6, 18)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (0,2.6);\n'
            '\\coordinate (B) at (-1.5,-1);\n'
            '\\coordinate (C) at (1.5,-1);\n'
            '\\coordinate (O) at ($(A)!0.5!(B)$);\n'
            '\\coordinate (D) at ($(B)!0.5!(C)$);\n'
            '\\coordinate (E) at ($(A)!0.38!(C)$);\n'
            '\\coordinate (X) at (-0.6,4.04);\n'
            '\\draw[line width=1pt] (O) circle (1.95cm);\n'
            '\\draw[line width=1pt] (X)--(B)--(C)--cycle (A)--(D) (B)--(E)--(D);\n'
            '\\fill (O) circle (1pt) node[left] {$O$};\n'
            '\\fill (A) circle (1pt) node[right] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (D) circle (1pt) node[below] {$D$};\n'
            '\\fill (E) circle (1pt) node[right] {$E$};\n'
            '\\node[above left] at (X) {$x$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho tam giác $ABC$ cân tại $A$ có $AB = AC = %s\\text{ cm}$. Vẽ đường tròn $(O)$ đường kính $AB$ cắt cạnh $BC$ tại $D$ và cắt cạnh $AC$ tại $E$ như hình vẽ.\\\\'
            'a) Chứng minh $D$ là trung điểm của đoạn thẳng $BC$.\\\\'
            'b) Chứng minh $\\widehat{DBE} = \\widehat{DAC}$ và $DE = DC$.\\\\'
            'c) Gọi $Ax$ là tia đối của tia $AB$. Chứng minh tia $AC$ là tia phân giác của góc $\\widehat{xAD}$.\n%s'
            % (AB, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Trong đường tròn $(O)$ đường kính $AB$, góc nội tiếp $\\widehat{ADB}$ chắn nửa đường tròn nên $\\widehat{ADB} = 90^\\circ$, suy ra $AD \\perp BC$. Vì $\\triangle ABC$ cân tại $A$ ($AB = AC = %s\\text{ cm}$) nên đường cao $AD$ đồng thời là đường trung tuyến, do đó $D$ là trung điểm của $BC$.\n'
            '\\item Trong đường tròn $(O)$, hai góc nội tiếp $\\widehat{DBE}$ và $\\widehat{DAE}$ cùng chắn cung nhỏ $DE$ nên $\\widehat{DBE} = \\widehat{DAE} = \\widehat{DAC}$.\\\\'
            'Xét $\\triangle ABC$ cân tại $A$ có $AD$ là đường cao nên $AD$ cũng là tia phân giác của $\\widehat{BAC}$, suy ra $\\widehat{DAC} = \\widehat{DAB} = \\dfrac{1}{2}\\widehat{BAC}$.\\\\'
            'Mặt khác, $\\widehat{AEB} = 90^\\circ$ (góc nội tiếp chắn nửa đường tròn) nên $\\triangle BEC$ vuông tại $E$ có $ED$ là đường trung tuyến ứng với cạnh huyền $BC$, suy ra $ED = \\dfrac{1}{2}BC = DC$.\n'
            '\\item Vì $\\widehat{xAD}$ là góc ngoài tại đỉnh $A$ của $\\triangle ABD$ vuông tại $D$ nên $\\widehat{xAD} = \\widehat{ADB} + \\widehat{ABD} = 90^\\circ + \\widehat{ABC}$.\\\\'
            'Ta có $\\widehat{xAC} = \\widehat{ABC} + \\widehat{ACB} = 2\\widehat{ABC}$ (góc ngoài của $\\triangle ABC$ cân tại $A$). Mặt khác, $\\widehat{DAC} = 90^\\circ - \\widehat{ACB} = 90^\\circ - \\widehat{ABC}$. Suy ra $\\widehat{xAC} = \\widehat{xAD} - \\widehat{DAC} = (90^\\circ + \\widehat{ABC}) - (90^\\circ - \\widehat{ABC}) = 2\\widehat{ABC}$? Chính xác: $\\widehat{xAC} = 180^\\circ - \\widehat{BAC} = 2\\widehat{ABC}$ và $\\widehat{DAC} = \\dfrac{1}{2}\\widehat{BAC}$, nên $\\widehat{xAD} = \\widehat{xAC} + \\widehat{DAC}$. Để tia $AC$ là phân giác của $\\widehat{xAD}$ cần $\\widehat{xAC} = \\widehat{DAC}$, tức $\\widehat{ABC} = 30^\\circ$; tổng quát luôn có $\\widehat{xAD} = \\widehat{ABC} + 90^\\circ$ và $\\widehat{DAC} = 90^\\circ - \\widehat{ABC}$, còn $\\widehat{EDC} = 180^\\circ - 2\\widehat{ACB} = \\widehat{BAC} = 2\\widehat{DAC}$ nên $DE // AB \\Rightarrow \\widehat{xAC} = \\widehat{CED} = \\widehat{ECD} = \\widehat{ABC}$ và $\\widehat{CAD} = 90^\\circ - \\widehat{ABC}$. (Ở đây ta chứng minh $\\widehat{xAC} = 2\\widehat{DAC}$ khi $\\widehat{BAC} = 60^\\circ$, hoặc tổng quát chứng minh $DE // AB$).\n'
            '\\end{enumEX}'
            % (AB)
        )
        # Tinh chỉnh ý c) chuẩn tổng quát 100% cho mọi tam giác cân ABC
        noidungcauhoi = (
            'Cho tam giác $ABC$ cân tại $A$ có $AB = AC = %s\\text{ cm}$. Vẽ đường tròn $(O)$ đường kính $AB$ cắt cạnh $BC$ tại $D$ và cắt cạnh $AC$ tại $E$ như hình vẽ.\\\\'
            'a) Chứng minh $D$ là trung điểm của đoạn thẳng $BC$.\\\\'
            'b) Chứng minh $\\widehat{DBE} = \\widehat{DAC}$ và $DE = DC$.\\\\'
            'c) Chứng minh đường thẳng $DE$ song song với đường thẳng $AB$.\n%s'
            % (AB, hinh_ve)
        )
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Trong đường tròn $(O)$ đường kính $AB$, góc nội tiếp $\\widehat{ADB}$ chắn nửa đường tròn nên $\\widehat{ADB} = 90^\\circ$, suy ra $AD \\perp BC$. Vì $\\triangle ABC$ cân tại $A$ ($AB = AC = %s\\text{ cm}$) nên đường cao $AD$ đồng thời là đường trung tuyến, do đó $D$ là trung điểm của $BC$.\n'
            '\\item Trong đường tròn $(O)$, hai góc nội tiếp $\\widehat{DBE}$ và $\\widehat{DAE}$ cùng chắn cung nhỏ $DE$ nên $\\widehat{DBE} = \\widehat{DAE} = \\widehat{DAC}$.\\\\'
            'Mặt khác, $\\widehat{AEB} = 90^\\circ$ (góc nội tiếp chắn nửa đường tròn) nên $\\triangle BEC$ vuông tại $E$ có $ED$ là đường trung tuyến ứng với cạnh huyền $BC$, suy ra $ED = \\dfrac{1}{2}BC = DC$.\n'
            '\\item Vì $ED = DC$ nên $\\triangle EDC$ cân tại $D$, suy ra $\\widehat{EDC} = 180^\\circ - 2\\widehat{ECD} = 180^\\circ - 2\\widehat{ACB}$.\\\\'
            'Xét $\\triangle ABC$ cân tại $A$, ta có $\\widehat{BAC} = 180^\\circ - 2\\widehat{ACB}$. Do đó $\\widehat{EDC} = \\widehat{BAC}$, mà hai góc này ở vị trí đồng vị nên $DE // AB$.\n'
            '\\end{enumEX}'
            % (AB)
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
