use agenda;
SELECT nome, telefone FROM contatos WHERE telefone IS NULL OR telefone = '';
desc contatos;
ALTER TABLE contatos MODIFY telefone VARCHAR(20) NOT NULL DEFAULT '';
UPDATE contatos SET telefone = '' WHERE telefone IS NULL;
SELECT nome, telefone FROM contatos ORDER BY id DESC LIMIT 5;
SELECT nome, contato FROM contatos;
SELECT nome, telefone FROM contatos WHERE usuario_id = 1;