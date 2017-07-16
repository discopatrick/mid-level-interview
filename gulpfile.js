var gulp = require('gulp');
var shell = require('gulp-shell');

gulp.task('test', shell.task([
  'python manage.py test'
]));

gulp.task('flake8', shell.task([
  'flake8 monitoring/ servers/ --exclude migrations'
]));

gulp.task('autopep8', shell.task([
    'autopep8 monitoring/ --in-place --recursive --exclude migrations',
    'autopep8 servers/ --in-place --recursive'
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
