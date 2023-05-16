pipeline
{
    options
    {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }

    agent any

    stages
    {
        stage('checkout Git Repo')
        {
            steps
            {
                script
                {
                     properties([pipelineTriggers([pollSCM('H/30 * * * *')])])
                }

                git 'https://github.com/yzion10/Python_Git_Jenkins_CourseProject.git'
            }
        }
        stage('job 1')
        {
            steps
            {
                script
                {
                    def isSuccess = false

                    try
                    {
                        bat "start /min C:\\DevOps\\GIT\\Python_Git_Jenkins_CourseProject\\venv\\Scripts\\python.exe rest_app.py"
                        isSuccess = true
                    }
                     finally
                    {
                        env.JOB1_SUCCESS = isSuccess.toString()
                    }
                }
            }
        }

        stage('job 2')
        {
            steps
            {
                script
                {
                    def isSuccess = false

                    try
                    {
                        bat "start /min C:\\DevOps\\GIT\\Python_Git_Jenkins_CourseProject\\venv\\Scripts\\python.exe web_app.py"
                        isSuccess = true
                    }
                    finally
                    {
                        env.JOB2_SUCCESS = isSuccess.toString()
                    }
                }
            }
        }

        stage('job 3')
        {
            when
            {
                expression
                {
                    env.JOB1_SUCCESS == 'true'
                }
            }
            steps
            {
                script
                {
                    def isSuccess = false

                    try
                    {
                        bat "C:\\DevOps\\GIT\\Python_Git_Jenkins_CourseProject\\venv\\Scripts\\python.exe backend_testing.py"
                        isSuccess = true
                    }
                    finally
                    {
                        env.JOB3_SUCCESS = isSuccess.toString()
                    }
                }
            }
        }

        stage('job 4')
        {
            when
            {
                expression
                {
                    env.JOB2_SUCCESS == 'true'
                }
            }
            steps
            {
                script
                {
                    def isSuccess = false

                    try
                    {
                        bat "C:\\DevOps\\GIT\\Python_Git_Jenkins_CourseProject\\venv\\Scripts\\python.exe fronted_testing.py"
                        isSuccess = true
                    }
                    finally
                    {
                        env.JOB4_SUCCESS = isSuccess.toString()
                    }
                }
            }
        }

        stage('job 5') {
            when
            {
                expression
                {
                    env.JOB1_SUCCESS == 'true' && env.JOB2_SUCCESS == 'true'
                }
            }
            steps
            {
                script
                {
                    bat "C:\\DevOps\\GIT\\Python_Git_Jenkins_CourseProject\\venv\\Scripts\\python.exe combined_testing.py"
                }
            }
        }

        stage('job 6')
        {
           when
            {
                expression
                {
                    env.JOB1_SUCCESS == 'true' && env.JOB2_SUCCESS == 'true'
                }
            }
            steps
            {
                bat "C:\\DevOps\\GIT\\Python_Git_Jenkins_CourseProject\\venv\\Scripts\\python.exe clean_environment.py"
            }
        }
    }
}