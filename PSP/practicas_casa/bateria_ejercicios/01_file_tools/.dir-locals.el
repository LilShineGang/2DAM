((python-mode . ((python-shell-interpreter . "python")
                 (dape-configs . ((debugpy
                                   modes (python-mode)
                                   command "python"
                                   command-args ("-m" "debugpy.adapter")
                                   :type "executable"
                                   :request "launch"
                                   :cwd dape-cwd-fn))))))
