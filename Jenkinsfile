pipeline
{
    options
    {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }

    environment
    {
        JOB1_SUCCESS = false
        JOB2_SUCCESS = false
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
                        bat "start /min C:\Python27amd64\python.exe rest_app.py"
                        isSuccess = true
                    }
                    catch (Exception e)
                    {
                        isSuccess = false
                        echo "Job 1 Error: ${e.getMessage()}"
                    }
                    finally
                    {
                        env.JOB1_SUCCESS = isSuccess
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
                        bat "start /min C:\Python27amd64\python.exe web_app.py"
                        isSuccess = true
                    }
                    catch (Exception e)
                    {
                        isSuccess = false
                        echo "Job 2 Error: ${e.getMessage()}"
                    }
                    finally
                    {
                        env.JOB2_SUCCESS = isSuccess
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
                    env.JOB1_SUCCESS
                }
            }
            steps
            {
                script
                {
                    try
                    {
                        bat "C:\Python27amd64\python.exe backend_testing.py"
                    }
                    catch (Exception e)
                    {
                        echo "Job 3 Error: ${e.getMessage()}"
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
                    env.JOB2_SUCCESS
                }
            }
            steps
            {
                script
                {
                    try
                    {
                        bat "C:\Python27amd64\python.exe fronted_testing.py"
                    }
                    catch (Exception e)
                    {
                        echo "Job 4 Error: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('job 5')
        {
            when
            {
                expression
                {
                    env.JOB1_SUCCESS && env.JOB2_SUCCESS
                }
            }
            steps
            {
                script
                {
                    try
                    {
                        bat "C:\Python27amd64\python.exe combined_testing.py"
                    }
                    catch (Exception e)
                    {
                        echo "Job 5 Error: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('job 6')
        {
           when
            {
                expression
                {
                    env.JOB1_SUCCESS && env.JOB2_SUCCESS
                }
            }
            steps
            {
                script
                {
                    try
                    {
                        bat "C:\Python27amd64\python.exe clean_environment.py"
                    }
                    catch (Exception e)
                    {
                        echo "Job 6 Error: ${e.getMessage()}"
                    }
                }
            }
        }
    }
}