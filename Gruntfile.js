module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        banner: '/*! <%= pkg.title || pkg.name %> - v<%= pkg.version %> - " + "<%= grunt.template.today(\"yyyy-mm-dd\") %>\n" + "<%= pkg.homepage ? \"* \" + pkg.homepage + \"\\n\" : \"\" %>" + "* Copyright (c) <%= grunt.template.today(\"yyyy\") %> <%= pkg.author.name %>;" + " Licensed <%= _.pluck(pkg.licenses, \"type\").join(\", \") %> */\n',

        src: {
            path: 'assets',
            css: '<%= src.path %>/css',
            font: '<%= src.path %>/font',
            img: '<%= src.path %>/img',
            js: '<%= src.path %>/js'
        },

        uglify: {
            build: {
                options: {
                    banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
                },
                files: {
                    'assets/js/all.min.js': [
                        '<%= src.js %>/vendor/jquery-1.10.1.js',
                        '<%= src.js %>/vendor/bootstrap.js',
                        '<%= src.js %>/vendor/jquery.pjax.js',
                        '<%= src.js %>/vendor/socialite.js',
                        '<%= src.js %>/notvanillae.js',
                        '<%= src.js %>/main.js'
                    ]
                }
            }
        },

        cssmin: {
            build: {
                options: {
                    banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
                },
                files: {
                    'assets/css/all.min.css': [
                        '<%= src.css %>/bootstrap.css',
                        '<%= src.css %>/bootstrap-responsive.css',
                        '<%= src.css %>/font-awesome.css',
                        '<%= src.css %>/notvanillae.css',
                        '<%= src.css %>/main.css'
                    ]
                }
            }
        }
    });

    // Load the plugins
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    // Default task(s).
    grunt.registerTask('default', ['uglify', 'cssmin']);
};