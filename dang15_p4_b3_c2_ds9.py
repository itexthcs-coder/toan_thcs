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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang15_p4_b3_c2_ds9(self):
    m_dd = random.choice([200, 300, 400, 500])
    c1 = random.choice([4, 5, 8, 10])
    c2 = random.choice([15, 20, 25])
    while c2 <= c1:
        c2 = random.choice([15, 20, 25])

    m_muoi = m_dd * c1 // 100
    ty_le_c2 = Rational(c2, 100)
    he_so_x = 1 - ty_le_c2
    vp_moi = m_dd * ty_le_c2 - m_muoi
    nghiem = vp_moi / he_so_x

    noidungcauhoi = (
        f"Một bình đang chứa ${m_dd}\\text{{ g}}$ dung dịch nước muối có nồng độ ${c1}\\%$. "
        f"Người ta muốn pha thêm muối tinh khiết vào bình để thu được dung dịch nước muối sát khuẩn có nồng độ ít nhất là ${c2}\\%$. "
        f"Hỏi cần pha thêm tối thiểu bao nhiêu gam muối tinh khiết?"
    )

    loigiai = (
        f"Khối lượng muối nguyên chất có sẵn trong bình là: ${m_dd} \\cdot {c1}\\% = {m_muoi}\\text{{ (g)}}$.\\\n"
        f"Gọi $x\\text{{ (g)}}$ là khối lượng muối tinh khiết cần pha thêm ($x > 0$).\\\n"
        f"Khi đó, khối lượng muối trong dung dịch mới là ${m_muoi} + x\\text{{ (g)}}$ và khối lượng dung dịch mới là ${m_dd} + x\\text{{ (g)}}$.\\\n"
        f"Để nồng độ dung dịch mới đạt ít nhất ${c2}\\%$, ta có bất phương trình:\\\n"
        f"$\\dfrac{{{m_muoi} + x}}{{{m_dd} + x}} \\ge \\dfrac{{{c2}}}{{100}}$\\\n"
        f"$100({m_muoi} + x) \\ge {c2}({m_dd} + x)$\\\n"
        f"${100 * m_muoi} + 100x \\ge {c2 * m_dd} + {c2}x$\\\n"
        f"${100 - c2}x \\ge {c2 * m_dd - 100 * m_muoi}$\\\n"
        f"$x \\ge {latex(nghiem)}$.\\\n"
        f"Vậy cần pha thêm tối thiểu ${latex(nghiem)}\\text{{ g}}$ muối tinh khiết."
    )

    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
