FROM registry.ar.bsch/santandertec/santander-tecnologia-docker-base-images-other-utilities:v2

RUN mkdir /root/.ssh                                # Create .ssh directo
RUN chmod 700 /root/.ssh                            # Set permissio
RUN touch /root/.ssh/known_hosts                    # Create known_hosts files
RUN chmod 600 /root/.ssh/known_hosts                # Set permissions
RUN ssh-keyscan -H wasmpkidesa.ar.bsch >> /root/.ssh/known_hosts  # Add server to known_hosts, "set sftp:auto-confirm" does not work
