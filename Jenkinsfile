pipeline{
    agent any

    stages{

        stage('Checkout'){
            steps{
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Install Dependencies'){
            steps {
                echo 'Installing dependencies...'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests'){
            steps{
                echo 'Running tests...'
                bat 'pytest lesson_12/ lesson_14/ -v --alluredir=allure-results'
            }
        }

        stage('Publish Results'){
            steps{
                echo 'Publishing test results...'
                allure([
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }

    post{
        always{
            mail(
                to: 'isaidima30@gmail.com',
                subject: "Jenkins Build ${currentBuild.fullDisplayName} - ${currentBuild.result}",
                body: """
Build: ${currentBuild.fullDisplayName}
Status: ${currentBuild.result}
URL: ${env.BUILD_URL}
                """
            )
        }
    }
}