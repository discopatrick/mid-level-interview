var gulp = require('gulp');
var shell = require('gulp-shell');

gulp.task('test', shell.task([
  'venv3.6/bin/python manage.py test'
]));

gulp.task('flake8', shell.task([
  'venv3.6/bin/flake8 monitoring/ servers/'
]));

gulp.task('watch', function(){
  gulp.watch(
    [
      './servers/**/*.py',
      './monitoring/**/*.py'
    ],
    ['flake8', 'test']
  )
})

gulp.task('default', ['test']);
