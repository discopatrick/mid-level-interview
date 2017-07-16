var gulp = require('gulp');
var shell = require('gulp-shell');

gulp.task('test', shell.task([
  'venv3.6/bin/python manage.py test'
]));

gulp.task('default', ['test']);
