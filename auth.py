from flask import Blueprint, redirect, request, render_template, flash, irl_for

auth_bp = Blueprint('auth_bp', __name__)