pipeline {
    agent any

    stages {
        stage('[OBJECTIF] Compilation application')
        {
            matrix
            {
                axes
                {
                    axis
                    {
                        name 'TARGET'
                        values 'project'
                    }
                    axis
                    {
                        name "RELEASEDEBUG"
                        values 'release','debug'
                    }
                }
                stages
            {
                stage('[WIN] Configuration environement.')
                {
                    steps
                    {
                        echo "Configuration env !"
                        echo "${TOTO}"
                        sh "pwd; ls"
                        sh "sh Hello.sh"     
                    }
                }
                stage('[WIN] Checkout Depot')
                {
                    steps
                    {
                        echo "Checkout depot."
                    }
                }
                stage('[LINUX] Compilation cible + warning')
                {
                    steps
                    {
                        echo "Compilation cible"
                    }
                }
                }
            }
        }
    }
}

