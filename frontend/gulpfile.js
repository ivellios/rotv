var gulp = require('gulp');
		sass = require('gulp-sass');
		path = require('path');
		concat = require('gulp-concat');
		uglify = require('gulp-uglifyjs');
		rename = require("gulp-rename");
	  cssmin = require('gulp-clean-css');
    runSequence = require('run-sequence');
		src = 'src/';
		dest = 'build/';
		static_dir = '../ro/static/';

    materialize = 'node_modules/materialize-css/bin/';

gulp.task('scripts', function() {
    return gulp.src([materialize+'materialize.js', src + 'js/*.js' ])
      	.pipe(concat('main.js'))
        .pipe(rename({suffix: '.min', basename: 'rotv'}))
        .pipe(uglify())
        .pipe(gulp.dest(dest + 'js'));
});

// Compile CSS from Less files
gulp.task('sass', function() {
    return gulp.src(src + 'sass/style.sass')
        .pipe(sass())
		.pipe(cssmin({restructuring: false, shorthandCompacting: false}))
		.pipe(rename({suffix: '.min', basename: 'rotv' }))
		.pipe(gulp.dest(dest + 'css'));
});

gulp.task('style', ['sass'], function() {
	return gulp.src([src + 'css/**/*' ])
		.pipe(gulp.dest(dest + 'css'));
});

gulp.task('fonts', function(){
    return gulp.src(['node_modules/materialize-css/fonts/**/*', src + 'fonts/**/*'])
      .pipe(gulp.dest(dest + 'fonts'));
});

gulp.task('images', function(){
    return gulp.src(src + 'images/**/*')
        .pipe(gulp.dest(dest + 'images'))
});

gulp.task('icons', function() { 
    return gulp.src('node_modules/font-awesome-sass/assets/fonts/**/*') 
        .pipe(gulp.dest(dest + 'fonts')); 
});

gulp.task('move_to_backend', function(){
    return gulp.src('build/**/*')
      .pipe(gulp.dest(static_dir))
});

gulp.task('watch_dev', ['build'], function() {
  // Watch .js files
 gulp.watch(src + 'js/*.js', ['build']);
  // Watch .less files
 gulp.watch([src + 'sass/**/*.sass', src + 'sass/**/*.scss'], ['build']);
  // Watch image files
 gulp.watch(src + 'images/**/*', ['build']);
});

gulp.task('build', function(){
  runSequence(['fonts', 'icons', 'style', 'scripts', 'images' ], 'move_to_backend');
});

gulp.task('default', ['fonts', 'style', 'scripts', 'images', 'watch_dev'])
