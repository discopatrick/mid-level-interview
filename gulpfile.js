var gulp = require('gulp');
var shell = require('gulp-shell');

gulp.task('test', shell.task([
  'echo testing'
]));

gulp.task('default', ['test']);
