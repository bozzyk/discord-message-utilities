pipeline {
    agent any
    stages {
        stage('Packages installation') {
            steps {
                script {
                    sh 'pip3 install -Ur requirements.txt'
                }
            }
        }
        stage('Load environment') {
            steps {
                script {
                    sh 'cp /home/captain/discord-message-utilities/variables.env $WORKSPACE/variables.env'
                }
            }
        }
        //stage('Static Code Check') {
        //    steps {
        //        script {
        //            sh 'find . -name \\*.py | xargs pylint -f parseable | tee pylint.log'
        //            recordIssues(
        //                tool: pyLint(pattern: 'pylint.log'),
        //                unstableTotalHigh: 100,
        //            )
        //        }
        //    }
        //}
        //stage('Unit tests run') {
        //    steps {
        //        script {
        //            sh 'pytest --with-xunit --xunit-file=pyunit.xml --cover-xml --cover-xml-file=cov.xml tests/*.py || true'
          //          step([
          //              $class: 'CoberturaPublisher',
          //              coberturaReportFile: "cov.xml",
          //              onlyStable: false,
          //              failNoReports: true,
          //              failUnhealthy: false,
          //              failUnstable: false,
          //              autoUpdateHealth: true,
          //              autoUpdateStability: true,
          //              zoomCoverageChart: true,
          //              maxNumberOfBuilds: 10,
          //              lineCoverageTargets: '80, 80, 80',
          //              conditionalCoverageTargets: '80, 80, 80',
          //              classCoverageTargets: '80, 80, 80',
          //              fileCoverageTargets: '80, 80, 80',
          //          ])
          //          junit "pyunit.xml"
          //      }
          //  }
        //}
        stage('Run the bot') {
            steps {
                script {
                    sh 'python3 $WORKSPACE/bot.py > $WORKSPACE/$(date +%Y%m%d).log'
                }
            }
        }
    }
}